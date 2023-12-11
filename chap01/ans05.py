text = "I am an NLPer"
 
def ngram(n, word):
    lis = []
    for i in range(len(word) - n + 1):
        lis.append(word[i:i+n])
    return lis
 
print(f"単語bi-gram:{ngram(2, text.split())}")
print(f"文字bi-gram:{ngram(2, text)}")