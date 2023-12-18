import sys

if len(sys.argv) != 2:
    print("引数不足")
    sys.exit(1)

n = int(sys.argv[1])

with open("popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line.strip())
