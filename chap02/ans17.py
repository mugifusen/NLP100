file_path = 'ans12-1.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    unique_strings = set(content.split())

unique_strings_count = len(unique_strings)

print("異なる文字列の集合の数:", unique_strings_count)
