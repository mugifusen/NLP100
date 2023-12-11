text1 = "paraparaparadise"
text2 = "paragraph"

def ngram(n, word):
    lis = []
    for i in range(len(word) - n + 1):
        lis.append(word[i:i+n])
    return lis
 
X = set(ngram(2, text1))
Y = set(ngram(2, text2))
 
print(f"X:{X}")
print(f"Y:{Y}")
print(f"和集合：{X | Y}")
print(f"積集合：{X & Y}")
print(f"差集合：{X - Y}")