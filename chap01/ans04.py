text4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 句読点を取り除き、単語に分解
words = text4.replace(".", "").split()

# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外は先頭の2文字を取り出す
word_dict = {}
for i, word in enumerate(words, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        word_dict[i] = word[:1]
    else:
        word_dict[i] = word[:2]

print(word_dict)
