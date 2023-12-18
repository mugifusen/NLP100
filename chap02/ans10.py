# ファイルを読み込む
with open("popular-names.txt", "r") as f:
    text = f.read()

# 行数カウント
lines = text.split("\n") #テキストを行ごとに分割
count = len(lines)

print(f"行数: {count}")
