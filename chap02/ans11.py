
# replaceだけでは空行が挟まるので、
# stripで文字列の先頭と末尾のホワイトスペース(空白・タブ・改行)を削除

with open("popular-names.txt") as f:
    for i in f:
        print(i.strip().replace("\t", " "))
