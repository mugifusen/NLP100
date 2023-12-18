import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
# set型のオブジェクトは一意な値のみが要素となる、要素の順序は保持されない
print(set(df.iloc[:,0]))