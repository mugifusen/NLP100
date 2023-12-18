
with open('popular-names.txt', 'r', encoding='utf-8') as input_file, \
     open('ans12-1.txt', 'w', encoding='utf-8') as output1_file, \
     open('ans12-2.txt', 'w', encoding='utf-8') as output2_file:
    for line in input_file:
        columns = line.strip().split()
        if len(columns) >= 2:  # 少なくとも2列以上ある行のみ処理
            output1_file.write(columns[0] + '\n')
            output2_file.write(columns[1] + '\n')        
