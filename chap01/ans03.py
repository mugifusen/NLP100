text3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 句読点を取り除き、単語に分解(空白で区切る)
words = text3.replace(",", "").replace(".","").split()

#print(words)

# 各単語のアルファベットの文字数をリストに格納
length = []
for word in words:
    length.append(len(word))

print(length)