import requests
import json
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('article')
    for link in links:
        print(link)

if __name__ == '__main__':
    html_doc = get_html('https://www.bloomberg.com/citylab')
    get_data(html_doc)
