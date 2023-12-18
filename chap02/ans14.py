import sys

file_path = "popular-names.txt"

if len(sys.argv) != 2:
    print("Usage: python script.py <N>")
    sys.exit(1)

n = int(sys.argv[1])

with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i < n:
            print(line.strip())
