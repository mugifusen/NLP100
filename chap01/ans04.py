text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = text.split()
one_word = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans_list = [word_list[i][0] if i+1 in one_word else word_list[i][:2] for i in range(len(word_list))]
print(ans_list)