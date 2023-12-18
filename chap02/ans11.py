# ファイルを読み込みモードで読み込む
with open("popular-names.txt", "r") as f:
    text = f.read()
    #readメソッド = ファイルの中身を文字列として変換

output = text.replace("\t"," ")
#replace = 置換（textのタブ文字を空白文字に）

with open("output.txt",'w') as w:
    w.write(output)#新しい文字列outputをoutput.txtに書きこむ。


