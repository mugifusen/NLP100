with open('ans12-1.txt', 'r', encoding='utf-8') as output1_file, \
     open('ans12-2.txt', 'r', encoding='utf-8') as output2_file, \
     open('ans13.txt', 'w', encoding='utf-8') as combined_output_file:
    lines_output1 = output1_file.readlines()
    lines_output2 = output2_file.readlines()

    for line_output1, line_output2 in zip(lines_output1, lines_output2):
        combined_output_file.write(line_output1.strip() + '\t' + line_output2.strip() + '\n')
