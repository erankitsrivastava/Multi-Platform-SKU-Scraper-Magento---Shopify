import requests
from bs4 import BeautifulSoup
import xlsxwriter
from urllib.parse import urljoin
import time

def scrape_magento_store(base_url, category_url):
    products = []
    
    # Get the category page
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find product links
    product_links = []
    product_items = soup.select('div.products.wrapper.grid.products-grid ol.product-items li.item.product.product-item')
    
    for item in product_items:
        link = item.select_one('a.product-item-link')
        if link and 'href' in link.attrs:
            product_links.append(link['href'])
    
    # Pagination handling (if needed)
    next_page = soup.select_one('a.action.next')
    if next_page and 'href' in next_page.attrs:
        print(f"Found next page: {next_page['href']}")
        products += scrape_magento_store(base_url, next_page['href'])
    
    # Process each product page
    for link in product_links:
        time.sleep(1)  # Be polite with delays between requests
        try:
            print(f"Processing Magento product: {link}")
            product_response = requests.get(link)
            product_soup = BeautifulSoup(product_response.text, 'html.parser')
            
            # Extract SKU - Magento stores it in multiple places, this is one common location
            sku_element = product_soup.select_one('div.product.attribute.sku div.value')
            if sku_element:
                sku = sku_element.text.strip()
                products.append({
                    'url': link,
                    'sku': sku,
                    'store': 'Magento'
                })
                print(f"Found SKU: {sku}")
            else:
                print(f"SKU not found for product: {link}")
        except Exception as e:
            print(f"Error processing {link}: {str(e)}")
    
    return products

def scrape_shopify_store(base_url, category_url):
    products = []
    page = 1
    
    while True:
        # Shopify often uses pagination with ?page= parameter
        paginated_url = f"{category_url}?page={page}"
        print(f"Processing Shopify page {page}: {paginated_url}")
        
        response = requests.get(paginated_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find product links
        product_links = []
        product_items = soup.select('div.grid__item div.card-wrapper')
        
        if not product_items:
            break  # No more products
            
        for item in product_items:
            link = item.select_one('a.full-unstyled-link')
            if link and 'href' in link.attrs:
                full_url = urljoin(base_url, link['href'])
                product_links.append(full_url)
        
        # Process each product page
        for link in product_links:
            time.sleep(1)  # Be polite with delays between requests
            try:
                print(f"Processing Shopify product: {link}")
                product_response = requests.get(link)
                product_soup = BeautifulSoup(product_response.text, 'html.parser')
                
                # Extract SKU - Shopify often has it in a meta tag or specific element
                sku_element = product_soup.select_one('span.variant-sku')
                if not sku_element:
                    # Alternative location
                    sku_element = product_soup.select_one('div.product__description__property[data-product-sku]')
                
                if sku_element:
                    sku = sku_element.text.strip()
                    if 'data-product-sku' in sku_element.attrs:
                        sku = sku_element['data-product-sku']
                    
                    products.append({
                        'url': link,
                        'sku': sku,
                        'store': 'Shopify'
                    })
                    print(f"Found SKU: {sku}")
                else:
                    print(f"SKU not found for product: {link}")
            except Exception as e:
                print(f"Error processing {link}: {str(e)}")
        
        page += 1
    
    return products

def save_to_excel(products, filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    
    # Write headers
    worksheet.write(0, 0, 'Store')
    worksheet.write(0, 1, 'SKU')
    worksheet.write(0, 2, 'URL')
    
    # Write data
    for row, product in enumerate(products, start=1):
        worksheet.write(row, 0, product['store'])
        worksheet.write(row, 1, product['sku'])
        worksheet.write(row, 2, product['url'])
    
    workbook.close()
    print(f"Data saved to {filename}")

def main():
    # Magento store
    magento_base = 'https://www.paint-by-numbers.store'
    magento_category = 'https://www.paint-by-numbers.store/themes/painting-by-numbers-masterpieces'
    
    # Shopify store
    shopify_base = 'https://mypaintlab.eu'
    shopify_category = 'https://mypaintlab.eu/collections/famous-artists'
    
    print("Starting Magento scrape...")
    magento_products = scrape_magento_store(magento_base, magento_category)
    
    print("\nStarting Shopify scrape...")
    shopify_products = scrape_shopify_store(shopify_base, shopify_category)
    
    # Combine results
    all_products = magento_products + shopify_products
    
    # Save to Excel
    save_to_excel(all_products, 'product_skus.xlsx')
    
    print(f"\nDone! Scraped {len(magento_products)} Magento products and {len(shopify_products)} Shopify products.")

if __name__ == '__main__':
    main()