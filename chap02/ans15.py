import pandas as pd

N = int(input())
df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(df.tail(N))