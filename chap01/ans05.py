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

c, w = N_gram(2, "I am an NLPer")
print("文字bi-gram",c)
print("単語bi-gram",w)