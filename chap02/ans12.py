import ans10

df1 = ans10.df.iloc[:, 0]
df2 = ans10.df.iloc[:, 1]

df1.to_csv("col1.txt", sep=",", header=False, index=False)
df2.to_csv("col2.txt", sep=",", header=False, index=False)