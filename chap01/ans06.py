def n_gram(n, s):
    return list(zip(*[s[i:] for i in range(n)]))

str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(n_gram(2, str1))
Y = set(n_gram(2, str2))
union = X | Y
intersection = X & Y
difference = X - Y

print('X:', X)
print('Y:', Y)
print('和集合:', union)
print('積集合:', intersection)
print('差集合:', difference)

print('Xにseが含まれるか:', {('s', 'e')} <= X)
print('Yにseが含まれるか:', {('s', 'e')} <= Y)