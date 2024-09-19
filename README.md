# web_scraper

A Python project to scrape data from websites using LLM (Large Language Models).

## Features

- Scrapes book information from [Books to Scrape](https://books.toscrape.com/)
- Extracts title, price, availability, rating, and image URL
- Saves the scraped data to a CSV file

## Requirements

- Python 3.x
- Required libraries: `pandas`, `scrapegraphai`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sushilsainju/web_scraper.git
   cd web_scraper
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variable for the API key:
   ```bash
   export SCRAPEOS_API_KEY='your_api_key_here'
   ```

## Usage

Run the script to start scraping:

bash
python main.py

The scraped data will be saved in `scraped_data.csv`.
