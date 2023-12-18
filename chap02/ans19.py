from collections import Counter

file_path = 'popular-names.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 1列目の文字列の出現頻度を計算
first_column_values = [line.split()[0] for line in lines]
frequency_counter = Counter(first_column_values)

# 出現頻度が高い順に並べ替えて表示
for value, count in frequency_counter.most_common():
    print(f"{value}: {count}回")
