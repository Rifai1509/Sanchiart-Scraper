import requests
from bs4 import BeautifulSoup
import json

url = 'http://sanchitart.in/artist-section.php'
headers = {
    'Referer': 'http://www.sanchitart.in/artist-section.php',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
r= requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
artists = soup.find('div','alphamenu1').findAll('li')


urls = []
for a in artists:
    url = f"http://sanchitart.in/{a.find('a')['href']}"
    # print(url)
    urls.append(url)
# print(urls)

with open('artist_urls.json', 'w', encoding='utf-8') as file:
    json.dump(urls, file)