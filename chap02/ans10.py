import sys

# コマンドライン引数でファイル名を指定
file_name = sys.argv[1]

# ファイルを読み込む
with open(file_name, "r") as f:
    text = f.read()

# 行数と文字数をカウント
lines = text.split("\n") #テキストを行ごとに分割
line_count = len(lines)

print(f"行数: {line_count}")

#確認方法wc -l popular-names.txt
#1少なく表示されたためtxt最終行に改行追加