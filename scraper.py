#$ python -m pip install requests
# This script scrapes a website and extracts data from specified HTML tags.

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_data(soup, tag, class_name=None):
    if soup is None:
        return []
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)
    return [element.get_text(strip=True) for element in elements]

def main():
    url = 'https://example.com'  # Replace with the target URL
    soup = scrape_website(url)
    
    if soup:
        titles = extract_data(soup, 'h1')  # Example: Extract all <h1> tags
        print("Extracted Titles:")
        for title in titles:
            print(title)
        # You can add more extraction logic here
        
if __name__ == "__main__":
    main()