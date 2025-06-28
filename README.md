# 🛍️ Multi-Platform SKU Scraper - Magento & Shopify

A Python-based SKU scraper that extracts product SKUs and URLs from Magento and Shopify e-commerce platforms. Designed for e-commerce analysts, product researchers, or developers looking to automate product catalog tracking across different storefronts.

---

## 🚀 Features

- 🔎 Scrapes product **SKUs** from both Magento and Shopify stores
- 🌐 Handles **pagination** automatically
- 🕵️ Extracts key info:
  - Product URL
  - Store Type (Magento/Shopify)
  - SKU (where available)
- 💾 Exports data to Excel (.xlsx) using `xlsxwriter`
- ⏱️ Adds polite request delays to avoid overwhelming servers

---

## 🛠️ Tech Stack

| Tool        | Purpose                              |
|-------------|---------------------------------------|
| `Python`    | Programming language                  |
| `requests`  | To send HTTP requests                 |
| `BeautifulSoup` | For parsing and scraping HTML      |
| `xlsxwriter` | For writing data to Excel files       |
| `time`      | For adding delay between requests     |
| `urllib.parse` | For handling URL joins              |

---

## 📁 Project Structure

```
sku_scraper/  
├── scraper.py            # Main scraper script  
├── product_skus.xlsx     # Output Excel file (after run)  
├── README.md             # Project documentation  
├── requirements.txt      # Python dependencies  
```



---

## ⚙️ How to Use

### 1. Clone the Repository
```
git clone  https://github.com/IkramDev512/Multi-Platform-SKU-Scraper-Magento---Shopify.git
cd sku-scraper
```
### 2. Install Requirements

```
pip install -r requirements.txt
```

### 3. Run the Scraper
```
python scraper.py

```
Output will be saved to product_skus.xlsx.

## 📊 Sample Output (Excel)
| Store   | SKU    | URL                                                          |
| ------- | ------ | ------------------------------------------------------------ |
| Magento | art-ab-046 | [https://example.com/product1](https://example.com/product1) |
| Shopify | MNZ-DY-040-en | [https://example.com/product2](https://example.com/product2) |

## 📬 About the Developer
Hi, I'm Ikram, a Python developer focused on web scraping, browser automation, and transitioning into Data Science. I specialize in building efficient scrapers for e-commerce, real estate, and medical platforms and other niches.

### 📫 For freelance projects: shahikram295@gmail.com
