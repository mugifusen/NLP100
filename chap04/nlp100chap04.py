import re
import sys

# 形態素解析結果を読み込む関数
def input_mecab(filename):
    # ファイル（neko.txt.mecab.txt）を開く
    with open(filename, 'r') as infile:
        # 小説全体
        sentences = []
        # 小説中の一文
        sentence = []
        for line in infile.readlines():
            # もし読み込んだ一行が空行だったら
            if line == 'EOS\n':
                # もしsentenceに要素が既に存在する場合
                # つまり「。」のつぎの「EOS」が来て、一文として完成する場合
                if len(sentence) > 0:
                    sentences.append(sentence)
                    sentence = []
                continue
            
            # 正規表現
            # "\t", "," で読み込んだ一行を分割
            sline = re.split('[,\t]', line)

            # エラー処理（起きるはずないと思うけどどうだろうか）
            if len(sline) < 8:
                print('### 読み込みエラー:\n', sline + '\n')
                sys.exit(1)

            # 辞書型としてsentenceにappendする
            # surface ... 表層形
            # bace    ... 基本形
            # pos     ... 品詞
            # pos1    ... 品詞細分類1
            sentence.append({'surface': sline[0], 'base':sline[7], 'pos':sline[1], 'pos1':sline[2]})

    print('** 読み込み完了 **\n')
    return sentences

# 問30を解くために
if __name__ == '__main__':
    filename = 'neko.txt.mecab.txt'
    sentences = input_mecab(filename)
    print('')
    print('mainとして実行されました。')