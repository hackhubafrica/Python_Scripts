import requests
from bs4 import BeautifulSoup
import json
import re

# Function to fetch HTML content from a URL
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch URL: {url}")

# Function to extract WhatsApp group links from HTML
def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    
    # Find all <a> tags with href containing 'chat.whatsapp.com'
    for link in soup.find_all('a', href=re.compile(r'chat\.whatsapp\.com')):
        links.append(link.get('href'))
    
    return links

# Main function
def main():
    url = 'https://wagrouplinks.net/kenya-whatsapp-group-links/'
    try:
        html_content = fetch_html(url)
        whatsapp_links = extract_links(html_content)
        
        # Save links to a JSON file
        with open('whatsapp_group_links.json', 'w') as f:
            json.dump(whatsapp_links, f, indent=4)
        
        print(f"Successfully scraped {len(whatsapp_links)} WhatsApp group links.")
        print("Saved links to whatsapp_group_links.json")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    main()
