**README 2: Book Product Scraper with Resume Feature**

---

# 📄 Product Page Scraper (BooksToScrape.com)

A Python scraper that extracts book details (title, price, stock, image URL) from the paginated listings on [BooksToScrape.com](https://books.toscrape.com). Incorporates resume functionality via a tracker file for uninterrupted scraping.

## 🌐 Website Target

* `https://books.toscrape.com/catalogue/page-1.html`

## ✨ Key Features

* Scrapes book title, price, availability, and image URL
* Automatically navigates pagination until no more pages (404 detected)
* Saves each page's data in `CSV_Books/Page_<num>.csv`
* Resume scraping using `page_num.txt`
* Graceful handling of network or user interruptions

## 💡 Example Use Case

Simulates scraping real e-commerce catalogs (e.g., Amazon, Flipkart, Daraz) for:

* Price tracking
* Inventory monitoring
* Competitive analysis

## 💪 Key Strength

The script maintains progress in `page_num.txt` and continues from the correct page after any stop, ensuring efficient, incremental data collection.

## 💻 Technologies & Modules

* Python
* BeautifulSoup
* requests
* pandas
* os

## ⚙️ How to Run

1. Ensure Python 3.x is installed.
2. Install dependencies:

   ```bash
   pip install beautifulsoup4 requests pandas
   ```
3. Run the scraper:

   ```bash
   python main.py
   ```

## 📂 Output

* **CSV files** in `CSV_Books/` (e.g., `Page_1.csv`, `Page_2.csv`, …)
* **Tracker file**: `page_num.txt`

## 📁 Suggested Repo Structure

```
book-product-scraper/
├── main.py
├── README.md
└── CSV_Books/      # Generated output
    ├── Page_1.csv
    └── ...
```

---
