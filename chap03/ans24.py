import pandas as pd
import re

df = pd.read_json('jawiki-country.json', lines=True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values

lines = UK[0].split('\n')
# re.findallをすると、直接正規表現に一致するすべての事例を持ってこれる.リストで返す
# searchして該当する行を探し、文字列の処理をする二度手間を減らせる
# 正規表現の?により非貪欲なマッチングを示す。つまり、最小限の文字列にマッチする
file_names = re.findall('ファイル:(.+?)\|', '\n'.join(lines))
print('\n'.join(file_names))

