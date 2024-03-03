import pandas as pd
import re
import requests

df = pd.read_json('jawiki-country.json', lines=True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values
lines = UK[0].split('\n')

pattern = re.compile('\|(.+?)\s*=\s*(.+)')
emp = re.compile('\`{2,}(.*?)\`{2,}')
in_link = re.compile('\[\[(.+?)\]\]')
brackets = re.compile('\{\{(.+?)\}\}')

dic = {}
for line in lines:
    match = re.search(pattern, line)
    if match:
        dic[match[1]] = match[2]
# sessionを作成
S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + dic['国旗画像'],
    "prop": "imageinfo",
    "iiprop":"url"
}
# GETリクエスト送信
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
for _, v in PAGES.items():
    print (v['imageinfo'][0]['url'])