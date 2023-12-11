def n_gram(n, s):
    return list(zip(*[s[i:] for i in range(n)]))

str = 'I am an NLPer'
words_bi_gram = n_gram(2, str.split())
chars_bi_gram = n_gram(2, str)

print('単語bi_gram:', words_bi_gram)
print('文字bi_gram:', chars_bi_gram)