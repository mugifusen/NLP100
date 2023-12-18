with open('col1.txt', 'r', encoding='utf-8') as f1, \
     open('col2.txt', 'r', encoding='utf-8') as f2, \
     open('ans13.txt', 'w', encoding='utf-8') as ansf:
    lines_output1 = f1.readlines()
    lines_output2 = f2.readlines()
    #各行を要素とするリストに格納

    for line_output1, line_output2 in zip(lines_output1, lines_output2):#zipでまとめて1つのイテレータ作成
        ansf.write(line_output1.strip() + '\t' + line_output2.strip() + '\n')
        #stripメソッドで各行の先頭と末尾の空白文字を削除
