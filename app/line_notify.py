import configparser
import os

import requests


class LineNotify:

    def send(self, message, image=None, sticker_package_id=None, sticker_id=None):
        # 設定ファイルの読み込み
        config = self.__read_config()
        api_url = config['LINE_NOTIFY']['Api_Url']
        access_token = config['LINE_NOTIFY']['Line_Notify_Access_Token']

        # ヘッダーの作成
        headers = {'Authorization': 'Bearer ' + access_token}

        # メッセージデータの作成
        message = '\n' + message
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id
        }
        # スタンプの設定
        # https://developers.line.biz/en/reference/messaging-api/#sticker-message

        files = {}
        if image is not None:
            files = {'imageFile': open(image, 'rb')}

        # API呼び出し
        requests.post(api_url, headers=headers, data=payload, files=files)

    @classmethod
    def __read_config(cls):
        # 設定ファイルのパス取得
        path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(path, 'config.ini')

        # 設定ファイルの読み込み
        return configparser.ConfigParser().read(config_path, encoding='utf-8')
