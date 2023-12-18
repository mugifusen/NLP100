
with open('popular-names.txt', 'r', encoding='utf-8') as f1, \
     open('col1.txt', 'w', encoding='utf-8') as f2, \
     open('col2.txt', 'w', encoding='utf-8') as f3:
    for line in f1:
        columns = line.strip().split()
        #line.strip() = 先頭と末尾の空白文字を取り除く
        #line.strip().strip() = lineを空白文字で分割
    
        if len(columns) >= 2:  # 少なくとも2列以上ある行のみ処理
            f2.write(columns[0] + '\n')
            f3.write(columns[1] + '\n')        
