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
git clone https://github.com/erankitsrivastava/Multi-Platform-SKU-Scraper-Magento---Shopify.git sku-scraper
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

Hi, I'm **Ankit Srivastava** — a web developer with strong experience in **e-commerce development** (Magento, Shopify, Adobe Commerce), **web scraping**, and **browser automation**.  
I build scalable systems that power online stores, automate workflows, and extract valuable insights from platforms across niches like **e-commerce**, **real estate**, and **healthcare**.  

Currently, I’m also transitioning into **Data Science**, combining my development expertise with data-driven problem solving.  

### 🔧 What I Do
- 🛒 Custom **e-commerce solutions** using Magento 2, Shopify, and Adobe Commerce  
- 🤖 **Web scraping & browser automation** for product data, pricing, and analytics  
- 📦 Marketplace integrations (Amazon, Joom, OnBuy, Miravia, Frugo, etc.)  
- 📊 Building pipelines for large-scale data collection and analysis  

### 📫 Get in Touch
- 📧 Email: [ankit@haxcode.com](mailto:ankit@haxcode.com)  
- 💬 WhatsApp: [Click here to chat](https://wa.me/919506373657)
- 🌐 Website: [www.haxcode.com](https://www.haxcode.com)
