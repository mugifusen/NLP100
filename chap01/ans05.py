def n_gram(words, n):
   '''
   与えられたリストからn-gramを作成
   s:文字列
   n:単語数
   '''
   ans = []
   for i in range(len(words) + 1 - n):
       ans.append(words[i:i+n])
   return ans

s = "I am an NLPer"

#単語bi-gram
words = s.split()
print(n_gram(words,2))

#文字bi-gram
letters = s.replace(' ','')
print(n_gram(letters,2))