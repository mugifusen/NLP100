with open("popular-names.txt") as f :
    for data in f:
        data = data.replace("\n", "")
        print(data.replace("\t", " "))