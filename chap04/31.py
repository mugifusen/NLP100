import nlp100chap04

sentences = nlp100chap04.input_mecab('neko.txt.mecab.txt')

for sentence in sentences:
    for mor in sentence:
        if mor['pos']=='動詞':
            print(mor['surface'])