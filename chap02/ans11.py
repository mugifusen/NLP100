# ファイルを読み込む
with open("popular-names.txt", "r") as f:
    text = f.read()

output = text.replace("\t"," ")

with open("output.txt",'w') as writer:
    writer.write(output)

#sed -e 's/\t/ /g' ./popular-names.txt
