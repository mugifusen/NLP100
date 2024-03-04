import nlp100chap04

sentences = nlp100chap04.input_mecab('neko.txt.mecab.txt')

noun_flag = False
no_flag = False
noun1: str

for sentence in sentences:
    for mor in sentence:
        # 前回のループでAが見つかっていない
        if noun_flag == False :
            # 今回でAが見つかった場合
            if mor['pos']=='名詞':
                noun_flag = True
                # Aをnoun1に格納
                noun1 = mor['surface']
        # 品詞Aが存在し、かつ「の」が見つかっていない場合
        elif noun_flag == True and no_flag == False:
            # Aの次に「の」が続く場合
            if mor['surface']=='の':
                no_flag = True
            else:
                # 全部白紙に戻す
                noun1 = ''
                noun_flag = no_flag = False
        # A「の」B が完成した状態の場合
        elif noun_flag == True and no_flag == True:
            if mor['pos']=='名詞':
                print(noun1+'の'+mor['surface'])
                noun_flag = no_flag = False