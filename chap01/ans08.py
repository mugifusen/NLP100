def cipher(str):
  rep = [chr(219 - ord(x)) if x.islower() else x for x in str]
  
  return ''.join(rep)

s = 'the quick brown fox jumps over the lazy dog'
s = cipher(s)
print('暗号化:', s)
s = cipher(s)
print('復号化:', s)