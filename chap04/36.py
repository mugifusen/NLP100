from matplotlib import pyplot
import japanize_matplotlib
import nlp100chap04

sentences = nlp100chap04.input_mecab('neko.txt.mecab.txt')

nouns = []

mor_freq = dict()

for sentence in sentences:
    for mor in sentence:
        # キーは(表層系, 品詞)のタプル。値は出現数。
        mor_freq.setdefault((mor['surface'], mor['pos']), 0)
        mor_freq[(mor['surface'], mor['pos'])] = mor_freq[(mor['surface'], mor['pos'])] + 1

ranking = sorted(mor_freq.items(), key=lambda i: i[1], reverse=True)

top10 = ranking[0:10]

x = []
y = []
for i in top10:
    x.append(i[0][0])
    y.append(i[1])

pyplot.bar(x, y)

# グラフタイトル
pyplot.title('頻度上位10語')

# グラフの軸
pyplot.xlabel('形態素')
pyplot.ylabel('頻度')

pyplot.show()