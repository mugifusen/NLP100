import pandas as pd
import re

df = pd.read_json('jawiki-country.json', lines=True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values

lines = UK[0].split('\n')
print(lines)
for line in lines:
    if re.search('Category', line):
        print(line)