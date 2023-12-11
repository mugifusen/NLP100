s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
n = 0
s_list = s.replace('.', ' .').split()
s_tapule = []
for i in s_list:
    n += 1
    if n in num:
        s_tapule.append((i[0],n))
    else:
        s_tapule.append((i[:2],n))

d = dict(s_tapule)
print(d)