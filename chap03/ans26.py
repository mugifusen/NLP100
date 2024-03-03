import pandas as pd
import re

df = pd.read_json('jawiki-country.json', lines=True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values

lines = UK[0].split('\n')
# {2,}は直前の正規表現が2以上という意味
pattern = re.compile('\|(.+?)\s*=\s*(.+)')
emp = re.compile('\`{2,}(.*?)\`{2,}')
dic = {}
for line in lines:
    match = re.search(pattern, line)
    # グルーピングした場合、置換後のマッチングした文字列を利用できる
    # デフォルトは\1,\2..のように1つ目、2つ目にマッチした箇所と対応
    # raw文字列でない普通の文字列の時はエスケープシーケンス必要
    if match:
        dic[match[1]] = match[2]
    match = re.sub(emp, '\\1', line)
    print(match)
    
# print(dic)