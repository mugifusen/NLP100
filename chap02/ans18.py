import pandas as pd
# sort_valuesでカラム名を指定し、ソートできる
# ascending=Falseを指定することで、降順
df = pd.read_csv('popular-names.txt', sep='\t', header=None)
df.sort_values(2, ascending=False)