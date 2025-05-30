import requests
from bs4 import BeautifulSoup

URL = 'https://www.gazeta.ru/sport/'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
html = requests.get(URL, headers=HEADER).text
soup = BeautifulSoup(html, features='html.parser')
articles = soup.find_all('div', class_='w_col2')
print(articles)