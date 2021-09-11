import csv
import datetime
import os

import pandas as pd
import requests

from app.line_notify import LineNotify


class BaseScraping:
    """ スクレイピングの既定クラス
    スクレイピング、結果の保存、前回の結果との比較、差分がある場合はLINE通知を行います。
    スクレイピングメソッドのみサイトによって実装が異なるため、サブクラスでオーバーライドします。
    """

    def __init__(self, log_file_name, base_url):
        self.log_file_name = log_file_name
        self.base_url = base_url

    def execute(self):
        # 前回のスクレイピング結果の取得
        last_result = self.read_last_csv()

        # スクレイピングの実行
        current_result = self.scraping()

        # 今回のスクレイピング結果を保存
        self.output_csv(current_result)

        # 今回と前回のスクレイピング結果の差分を抽出
        diff_list = self.get_diff(current_result, last_result)

        if diff_list:
            # 差分がある場合のみLINEに通知
            self.send_to_line(diff_list)
        else:
            print(str(datetime.datetime.today()) + ":" + self.log_file_name + ':変更なし')

    def scraping(self):
        # サブクラスで実装
        return []

    def get_page(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        return requests.get(url, headers=headers)

    def read_last_csv(self):
        if not os.path.exists(self.log_file_name):
            raise FileNotFoundError('ファイルがありません。')
        if os.path.getsize(self.log_file_name) == 0:
            raise FileNotFoundError('ファイルの中身が空です。')
        csv_list = pd.read_csv(self.log_file_name, header=None).values.tolist()
        return csv_list

    def output_csv(self, result):
        with open(self.log_file_name, 'w', newline='', encoding='utf_8') as file:
            headers = ['Title', 'URL']
            writer = csv.writer(file)
            writer.writerow(headers)
            for row in result:
                writer.writerow(row)

    def get_diff(self, current_result, last_result):
        diff_list = []
        for tmp in current_result:
            if tmp not in last_result:
                diff_list.append(tmp)
        return diff_list

    def send_to_line(self, diff_list):
        message = ''
        for tmp in diff_list:
            message += tmp[0] + '\n' + tmp[1] + '\n'
        bot = LineNotify()
        bot.send(message=message)
