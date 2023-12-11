#答え見ました
def N_gram(n, text):
    # 受け取ったtextの空白をなくす（1つの文字列にする）
    char = text.replace(" ", "")
    #print(char)

    # 受け取ったtextを単語に分解
    word = text.split()
    #print(word)

    char_list = []
    word_list = []
    for ch in range(len(char)):
        char_list.append(char[ch:n+ch])
    for wch in range(len(word)):
        word_list.append(word[wch:n+wch])
    return char_list, word_list

text6a = "paraparaparadise"
text6b = "paragraph"
A_bi, _ = N_gram(2, text6a)# 05.n-gramで使った関数
B_bi, _ = N_gram(2, text6b)# 05.n-gramで使った関数
#print(A_bi)
#print(B_bi)
X = set(A_bi)
Y = set(B_bi)
#print(X)
#print(Y)
print("和集合: ", X | Y)
print("積集合: ", X & Y)
print("差集合: ", X - Y)

checkword = "se"
if checkword in X and checkword in Y:
  print("XとYに{}が含まれる".format(checkword))
elif checkword in X:
  print("Xに{}が含まれる".format(checkword))
elif checkword in Y:
  print("Yに{}が含まれる".format(checkword))
else:
  print("{}はXとYには含まれない".format(checkword))