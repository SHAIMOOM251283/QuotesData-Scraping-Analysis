import requests
from bs4 import BeautifulSoup
import re

class ExtractLinks:

    def __init__(self):
        self.base_url = "https://quotes.toscrape.com"
        self.tags = set()  # Using a set to avoid duplicates

    def scrape_tags(self):
        next_page = "/page/1"
        page_number = 1 

        while next_page:
            print(f"Extracting tags from Page {page_number}")

            response = requests.get(self.base_url + next_page)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all tag links
            tag_elements = soup.find_all('a', class_='tag')
            for tag in tag_elements:
                self.tags.add(tag.text)

            # Find the 'Next' button using the pager navigation
            next_button = soup.find('ul', class_='pager').find('li', class_='next')
            if next_button:
                txtNext = next_button.find('a').get_text()

                # Check if the text contains 'Next' using regex
                if re.findall(r".*(Next).*", txtNext):
                    next_page = next_button.find('a')['href']
                else:
                    next_page = None  # No valid 'Next' button found
            else:
                next_page = None  # No more pages
            
            page_number += 1

    def construct_url(self):
        print("\nLOADED")
        select = input("Type 'homepage' or 'tag': ").lower().strip()
    
        if select == 'homepage':
            print(f"\nSelected URL: {self.base_url}")
            return self.base_url
              
        else:
            print("\n***ALL TAGS***")
            for tag in self.tags:
                print(tag)

            selected_tag = input("\nEnter tag (e.g. 'love'): ").lower().strip()
            link_url = f"{self.base_url}/tag/{selected_tag}"
            print(f"\nSelected URL: {link_url}")
            return link_url

    def run(self):
        self.scrape_tags()
        return self.construct_url()
        
if __name__ == '__main__':
    extraction = ExtractLinks()
    extraction.run()
