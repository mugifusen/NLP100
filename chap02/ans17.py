with open('ans12-1.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    string = set(content.split())
    #得られた単語のリストからユニークな要素を取り出し、それらを含む集合 string を作成
count = len(string)

print("異なる文字列の集合の数:", count)
