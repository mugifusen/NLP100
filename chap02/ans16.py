import ans10

n = 2
idx = ans10.df.shape[0] // n
for i in range(n):
    df_split = ans10.df.iloc[i * idx:(i + 1) * idx]
    df_split.to_csv(f"popular-names{i}.txt", sep="\t",header=False, index=False)