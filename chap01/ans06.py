s1 = "paraparaparadise"
s2 = "paragraph"

def n_gram(word, n):
   '''
   与えられたリストからn-gramを作成
   s:文字列
   n:単語数
   '''
   ans = []
   for i in range(len(word) + 1 - n):
       ans.append(word[i:i+n])
   return ans

X = n_gram(s1,2)
print('X', X)
Y = n_gram(s2,2)
print('Y', Y)

#和集合
s_union = set(X) | set(Y)
#s_union = set(X).union(set(Y))
print('和集合',s_union)

#積集合
s_intersection = set(X) & set(Y)
#s_intersection = set(X).intersection(set(Y))
print('積集合', s_intersection)

#差集合
s_difference = set(X) - set(Y)
#s_difference = set(X).difference(set(Y))
print('差集合', s_difference)

#'se'が含まれているか
print('"se"が含まれているか')
print('X', 'se' in X)
print('Y', 'se' in Y)