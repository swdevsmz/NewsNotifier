# News Notifier

ニュースサイト等をスクレイピングして、前回より変更があった場合に
LINEに通知するアプリケーションです。

## 実行環境の構築
### venv作成
~~~bash
python -m venv venv
~~~

### venv起動方法 
~~~bash
source ./venv/Scripts/activate
~~~
※Windows上のGit Bashの場合

### venv終了方法
~~~bash
deactivate
~~~
### pipを利用してライブラリの一括インストール
~~~bash
pip install -r requirements.txt
~~~

## Line Api Tokenの設定
https://notify-bot.line.me/ja/  

上記ページよりアカウント作成後、

`マイページ > トークンを発行する > トークン名、トークルームを設定 > 発行する  `
発行されたトークンを`config.ini`の`Line_Notify_Access_Token`に設定する


## アプリケーションの実行
~~~bash
python main.py
~~~