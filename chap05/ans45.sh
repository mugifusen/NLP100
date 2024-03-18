#コーパス中で頻出する述語と格パターンの組み合わせ
cat ./result45.txt | sort | uniq -c | sort -nr | head -n 5
#「行う」「なる」「与える」という動詞の格パターン
cat ./result45.txt |grep "行う" | sort |uniq -c | sort -nr |head -n 5
cat ./result45.txt |grep "なる" | sort |uniq -c | sort -nr |head -n 5
cat ./result45.txt |grep "与える" | sort |uniq -c | sort -nr |head -n 5
