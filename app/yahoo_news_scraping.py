import os

from bs4 import BeautifulSoup

from app.base_scraping import BaseScraping


class YahooNewsScraping(BaseScraping):
    LOG_FILE_NAME = os.path.dirname(__file__) + os.sep + 'log' + os.sep + 'last_yahoo_news_log.csv'
    BASE_URL = 'https://news.yahoo.co.jp/topics/top-picks'

    def __init__(self):
        super(YahooNewsScraping, self).__init__(self.LOG_FILE_NAME, self.BASE_URL)

    def scraping(self):
        # リクエストを送信してページを取得
        response = super(YahooNewsScraping, self).get_page(self.BASE_URL)

        # ページを解析し、ニュースフィードのリンクタグを取得
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all(class_='newsFeed_item_link')

        # タグからスクレイピング結果を作成
        return list(map(self.__create_result, tags))

    @classmethod
    def __create_result(cls, tag):
        return [
            tag.text,
            tag.get('href')
        ]
