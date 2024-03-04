import nlp100chap04

sentences = nlp100chap04.input_mecab('neko.txt.mecab.txt')

# 名詞を格納するリスト
nouns = []

for sentence in sentences:
    for mor in sentence:
        # もし名詞なら
        if mor['pos']=='名詞':
            nouns.append(mor['surface'])
        else:
            # リストに名詞がたまっている場合
            if len(nouns) > 1:
                # 全ての名詞を吐き出す
                for i in nouns:
                    print(i+' ', end='')
                print('')
            # リストを空にする
            nouns = []