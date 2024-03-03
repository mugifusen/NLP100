import pandas as pd
import re

df = pd.read_json('jawiki-country.json', lines=True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values

lines = UK[0].split('\n')
#  キーの箇所に?付けるとうまく読み取れない
pattern = re.compile('\|(.+?)\s*=\s*(.+)')
dic = {}
for line in lines:
    match = re.search(pattern, line)
    if match:
        # match[0]にはマッチした全体の文字列が入る.
        # つまりmatch[0]には"|キー = 値"という文字列が格納されてる
        dic[match[1]] = match[2]
print(dic)