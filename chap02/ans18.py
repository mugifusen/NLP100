file_path = 'popular-names.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 3列目の数値でソート
sorted_lines = sorted(lines, key=lambda line: int(line.split()[2]), reverse=True)

# ソートされた結果をファイルに保存
with open("ans18.txt", 'w', encoding='utf-8') as output_file:
    output_file.writelines(sorted_lines)
