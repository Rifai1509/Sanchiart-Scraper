import requests
# import html5lib
from bs4 import BeautifulSoup
# import pandas as pd

url = 'http://www.sanchitart.in/Arpana-Caur-2.html'
headers = {
    'Referer': 'http://www.sanchitart.in/artist-section.php',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
r= requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
artist = soup.find('div','artists_name_blk').find('strong').text.strip()
product = soup.find('div',{'id':'slider'}).find_all('li', {'style':'border-top:0px;border-bottom:0px;'})

lot = 0
for p in product:
    lot += 1
    title = p.find('td',{'align':'center'}).text.strip()
    table = p.find('td', {'valign':'top'}).findAll('tr')
    desc = table[0].text.split('\n')[2].strip()
    medium = table[1].text.split('\n')[2].strip().replace('..','paper')
    year = table[2].text.split('\n')[2].strip()
    price = table[3].text.split('\n')[2].strip()
    url = p.find('td',{'align':'center'}).find('a')['href']
    availability = table[4].text.split('\n')[2].strip()
    img = f"http://www.sanchitart.in/{p.find('img')['src'].replace(' ','%20')}"

    print(lot)
    print(title)
    print(artist)
    print(price)
    print(medium)
    print(desc)
    print(url)
    print(year)
    print(img)
    print(availability)
