import pandas as pd

N = int(input())
df = pd.read_csv('popular-names.txt', sep='\t', header=None)
d_n = len(df) // N
for i in range(N):
    df_s = df.iloc[i*d_n:(i+1)*d_n]
    print(df_s)