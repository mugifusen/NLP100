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

for i in ranking:
    print(i)