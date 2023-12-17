with open("popular-names.txt") as f:
    count = sum([1 for i in f])
print(count)