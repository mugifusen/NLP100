import MeCab
from MeCab import Tagger
import ipadic

# 辞書データの作成
analyser: Tagger = MeCab.Tagger(ipadic.MECAB_ARGS)

# neko.txtの読み込み
with open('./neko.txt', 'r') as infile:
    lines = infile.readlines()

# neko.txt.mecab.txtへ書き込み
with open('./neko.txt.mecab.txt', 'w') as outfile:
    for line in lines:
        result = analyser.parse(line)
        outfile.write(result)