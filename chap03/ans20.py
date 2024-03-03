# JSON形式のファイルをwget, gzip -d file-nameを用いて取得
# pandasではgzipのままで直接読み込み可能
# データフレームでjsonファイルを操作.各行で別々のJSONオブジェクトの為lines = Trueとした
# df['title']でbool型で指定箇所のみtrueになり、df[]にはtrueとなった箇所のみ抽出
# valuesでSeries->NumPy配列に変換し、リスト操作を可能にする
import pandas as pd

df = pd.read_json('jawiki-country.json', lines = True)
UK = df.loc[df['title'] == 'イギリス', 'text'].values

print(UK)