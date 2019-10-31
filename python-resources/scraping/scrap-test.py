import requests
from bs4 import BeautifulSoup
url   = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
html  = requests.get(url).text
doc   = BeautifulSoup(html, 'html.parser')
table = doc.find('table', class_='infobox vevent')
rows  = table.find_all('tr')
link  = rows[11].find('a')['href']
ver   = rows[6].find('div').text.split()[0]
url_i = rows[0].find('img')['src']
image = requests.get(f'https:{url_i}').content
with open('test.png', 'wb') as file:
    file.write(image)
print(link, ver)
