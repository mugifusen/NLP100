text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
 
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
 
dic = {}
 
text_r = text.replace(".", "")
text_lis = text_r.split()
for i, v in enumerate(text_lis):
    if i + 1 in num:
        dic[v[0]] = i + 1
    else:
        dic[v[:2]] = i + 1
 
print(dic)