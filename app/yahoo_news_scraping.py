import os

from bs4 import BeautifulSoup

from app.base_scraping import BaseScraping


class YahooNewsScraping(BaseScraping):
    LOG_FILE_NAME = os.path.dirname(__file__) + os.sep + 'log' + os.sep + 'last_yahoo_news_log.csv'
    BASE_URL = 'https://news.yahoo.co.jp/topics/top-picks'

    def __init__(self):
        super(YahooNewsScraping, self).__init__(self.LOG_FILE_NAME, self.BASE_URL)

    def scraping(self):
        response = super(YahooNewsScraping, self).get_page(self.BASE_URL)

        soup = BeautifulSoup(response.text, 'html.parser')

        tags = soup.find_all(class_='newsFeed_item_link')

        result = []
        for tag in tags:
            result.append([
                tag.text,
                tag.get('href')
            ])
            
        return result
