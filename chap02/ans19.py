import pandas as pd
# value_countsで出現度頻度の高い順に出力できる
df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(df[0].value_counts())