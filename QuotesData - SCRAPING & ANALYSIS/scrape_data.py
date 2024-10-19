import scrape_link_tags
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse
import logging

class QuotesScraper:
    
    def __init__(self):
        link_extractor = scrape_link_tags.ExtractLinks()
        self.selected_url = link_extractor.run()
        self.multi_page = False
        self.dataSet = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
        }
        logging.basicConfig(level=logging.INFO)
        
    def detect_if_multi_page(self):
        try:
            response = requests.get(self.selected_url, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Error detecting multi-page: {e}")
            return
        
        source = BeautifulSoup(response.content, 'html.parser')
        pager = source.find('ul', 'pager').find('li', 'next')
        if pager:
            self.multi_page = True
            self.url = f"{self.selected_url}/page/"
            logging.info(f"Multiple URLs detected: {self.url}")
        else:
            logging.info(f"Single URL detected: {self.selected_url}")
    
    def extract_data(self, source):
        for quotes in source.find_all('div', 'quote'):
            author = quotes.find(attrs={'class': 'author'}).get_text().strip()
            quote = quotes.find(attrs={'itemprop': 'text'}).get_text().strip()
            
            self.dataSet.append({
                'author': author,
                'quote': quote
            })
    
    def process_single_page(self):
        try:
            response = requests.get(self.selected_url, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Error processing single page: {e}")
            return
        
        source = BeautifulSoup(response.content, 'html.parser')
        self.extract_data(source)
    
    def process_multiple_pages(self):
        page = 1
        
        while True:
            logging.info(f"Scraping Page {page}")
            try:
                response = requests.get(self.url + str(page), headers=self.headers)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"Failed to retrieve page {page}, error: {e}")
                break
            
            source = BeautifulSoup(response.content, 'html.parser')
            self.extract_data(source)
            
            next_page = source.find('ul', 'pager').find('li', 'next')
            if not next_page:
                break
            
            page += 1
    
    def save_to_csv(self):
        if not self.dataSet:
            logging.warning("No data to save.")
            return
        
        df = pd.DataFrame(self.dataSet)
        parsed_url = urlparse(self.url if self.multi_page else self.selected_url)
        path_parts = parsed_url.path.strip('/').split('/')
        
        if len(path_parts) == 1 and path_parts[0] == 'page':
            slug = 'all_quotes'
        elif 'tag' in path_parts:
            slug = path_parts[path_parts.index('tag') + 1]
        else:
            slug = 'unknown'
        
        filename = f'data/{slug}.csv'
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")
    
    def run(self):
        self.detect_if_multi_page()
        if self.multi_page:
            self.process_multiple_pages()
        else:
            self.process_single_page()
        self.save_to_csv()

if __name__ == '__main__':
    while True:
        scraper = QuotesScraper()
        scraper.run()

        another = input("\nDo you want to scrape another URL? (yes/no): ").strip().lower()
        
        if another != 'yes':
            print("Exiting the scraper.")
            break 