original = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
original = original.replace(',', '')
original = original.replace('.', '')
original_list = original.split(' ')
word_num_list = [len(s) for s in original_list]
print(word_num_list)