s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
s_list = s.replace('.', ' .').split()
s_lengths = list(map(len, s_list))
print(s_lengths)