import os

import requests
import configparser


class LineNotify:

    def send(self, message, image=None, sticker_package_id=None, sticker_id=None):

        config = self.read_config()

        api_url = config['LINE_NOTIFY']['Api_Url']
        headers = {'Authorization': 'Bearer ' + config['LINE_NOTIFY']['Line_Notify_Access_Token']}

        message = '\n' + message
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id
        }
        files = {}
        if image is not None:
            files = {'imageFile': open(image, 'rb')}

        # API呼び出し
        requests.post(api_url, headers=headers, data=payload, files=files)


    def read_config(self):
        path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(path, 'config.ini')

        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')

        return config
