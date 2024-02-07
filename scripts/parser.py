import requests
from bs4 import BeautifulSoup
import json
import time
from scripts.rehash import text_rehash_ua

class Parser:
    def railway_parser(base_url:str)->list(dict()):
        """
        Parsing 2 news from www.railway.supply/uk/news-ua/
        --------------------------------------
        |str(base_url) - Basic url           |
        |return        - list({dict(news)})  |
        --------------------------------------
        """
        info = list()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        blocks = soup.find_all('div', class_='d-md-flex d-block flex-column justify-content-center')[:2]
        try:
            for el in blocks:
                description = str()
                date = el.find('p', class_='publish-date mb-2').text.replace(' ', '')
                title = el.find('a').text
                info_link = el.find('a')['href']
                new_request = BeautifulSoup(requests.get(info_link, headers=headers).text, 'lxml')
                for _ in new_request.find_all('span', class_='s1'):
                    description += _.text
                info.append({
                    'link': info_link,
                    'title': title,
                    'date': date,
                    'description': description,
                    'rehashed_description': text_rehash_ua(description)
                })
        except:
            time.sleep(5)
        return info

    def uzgov_parser(base_url:str)->list(dict()):
        """
        Parsing 2 news from www.uz.gov.ua
        --------------------------------------
        |str(base_url) - Basic url           |
        |return        - list({dict(news)})  |
        --------------------------------------
        """
        info = list()

        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'lxml')

        blocks_titles = soup.find_all('div', class_='block-title')

        for el in blocks_titles:
            description = str()
            date = el.find('div', class_='date').text
            title = el.find('a').text
            info_link = f"{base_url}{el.find('a')['href']}"
            new_request = BeautifulSoup(requests.get(info_link).text, 'lxml')
            for _ in new_request.find('div', class_='body'):
                description += _.text
            info.append({
                'link': info_link,
                'title': title,
                'date': date,
                'description': description,
                'rehashed_description': text_rehash_ua(description)
            })
        return info