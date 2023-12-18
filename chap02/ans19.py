from collections import Counter
#Counter クラスは、イテラブル（リスト、タプル、文字列など）内の各要素の出現回数を数えるための便利なクラスです。
with open('popular-names.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 1列目の文字列の出現頻度を計算
first_label = [line.split()[0] for line in lines]
most_label = Counter(first_label)
#Counter：リスト内の出現頻度を計算して結果を格納

# 出現頻度が高い順に並べ替えて表示
for value, count in most_label.most_common():
    #most_commonメソッド：出現頻度が高い順に要素と出現回数を返す
    print(f"{value}: {count}回")
