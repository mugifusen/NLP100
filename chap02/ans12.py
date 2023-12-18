import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
df.iloc[:,0].to_csv('col1.txt', sep=' ',header=False, index=False)
df.iloc[:,1].to_csv('col2.txt', header=False, index=False)
