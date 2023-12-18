cut -f 1 popular-names.txt | sort | uniq -c | sort -nr
#uniq -c : 連続した重複した行を1行にまとめ、その前に出現回数を付加
#sort -nr 出現回数を降順でソート