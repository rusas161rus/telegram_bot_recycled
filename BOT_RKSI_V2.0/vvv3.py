from bs4 import BeautifulSoup
import random
import json
import requests
import datetime
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'accept': 'application/json, text/plain, */*',
    'user-Agent': ua.google,
}

article_dict = {}

for i in range(1, 4):
    url = f'https://habr.com/ru/top/daily/page{i}/'

    req = requests.get(url, headers=headers).text

    soup = BeautifulSoup(req, 'lxml')
    all_hrefs_articles = soup.find_all('a', class_='tm-article-snippet__title-link') # получаем статьи

    for article in all_hrefs_articles: # проходимся по статьям
        article_name = article.find('span').text # собираем названия статей
        article_link = f'https://habr.com{article.get("href")}' # ссылки на статьи
        article_dict[article_name] = article_link

with open(f"articles_{datetime.datetime.now().strftime('%d_%m_%Y')}.json", "w", encoding='utf-8') as f: 
    try:    
        json.dump(article_dict, f, indent=4, ensure_ascii=False)
        print('Статьи были успешно получены')
    except:
        print('Статьи не удалось получить')