# mecab < neko.txt > neko.txt.mecabでneko.txt.mecabを作成
# read()でファイル全体を文字列として取得.splitでリストに変換
with open('neko.txt.mecab') as f:
    lines = f.read().split('\n')

# 出力は表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音となってる
result = []
for line in lines:
    l = line.split('\t')
    # EOSや空行を除く
    if (len(l) == 2):
        l_2 = l[1].split(',')
        # baseを活用型と仮定
        dic = {'surface':l[0], 'base':l_2[4], 'pos':l_2[0], 'pos1':l_2[1]}
        result.append(dic)
print(result)