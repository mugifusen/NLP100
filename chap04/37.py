from matplotlib import pyplot
import japanize_matplotlib
import nlp100chap04

sentences = nlp100chap04.input_mecab('neko.txt.mecab.txt')

nouns = []

tmp_count = dict()
co_cat_count = dict()
cat_flag = False

for sentence in sentences:
    for mor in sentence:
        # キーは(表層系, 品詞)のタプル。値は出現数。
        tmp_count.setdefault((mor['surface'], mor['pos']), 0)
        tmp_count[(mor['surface'], mor['pos'])] = tmp_count[(mor['surface'], mor['pos'])] + 1
        if mor['surface'] == '猫':
            cat_flag = True

    if cat_flag == True:
        for k, v in tmp_count.items():
            co_cat_count.setdefault(k, 0)
            co_cat_count[k] = co_cat_count[k] + v
        cat_flag = False
    tmp_count = {}

ranking = sorted(co_cat_count.items(), key=lambda i: i[1], reverse=True)

top10 = ranking[0:10]

x = []
y = []
for i in top10:
    x.append(i[0][0])
    y.append(i[1])

pyplot.bar(x, y)

# グラフタイトル
pyplot.title('「猫」と共起頻度の高い上位10語')

# グラフの軸
pyplot.xlabel('形態素')
pyplot.ylabel('頻度')

pyplot.show()