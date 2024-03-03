import pandas as pd
import re

df = pd.read_json('jawiki-country.json', lines=True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values

# 同じ正規表現で何度もマッチングを取る際はre.compileでコンパイルしてオブジェクトにしとくと効率良い
# ^:文頭、+:直前の正規表現を1以上繰り返される、.*:.は任意の文字で*は0回以上繰り返される、$:末尾
pattern = re.compile('^=+.*=+$')
lines = UK[0].split('\n')
for line in lines:
    if re.search(pattern, line):
        # levelは==を1として、===は2のように増加する.
        level = int(line.count('=')/2 - 1)
        print(line.replace('=', ''), level)
        


