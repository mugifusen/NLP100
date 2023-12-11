original = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
original = original.replace(',', '')
original = original.replace('.', '')
original_list = original.split(' ')

head_index_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
head_index_list_for_python = [i - 1 for i in head_index_list]

diction = {}

for i in range(len(original_list)):
    if i in head_index_list_for_python:
        diction[i] = original_list[i][:1]
    else:
        diction[i] = original_list[i][:2]

print(diction)