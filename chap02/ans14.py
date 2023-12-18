import sys#コマンドライン引数の取得

if len(sys.argv) != 2:
    print("引数不足")
    sys.exit(1)

n = int(sys.argv[1])

with open("popular-names.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):#enumerate = 要素のインデックスと要素を同時に取り出す
        if i < n:
            print(line.strip())
