# cutはファイルの各行をカットし、標準出力に出す
# -fオプションで切り出すフィールドを指定
cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt