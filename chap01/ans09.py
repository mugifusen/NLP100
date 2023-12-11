# 答え見ました。
import random
text09 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
text09 = text09.replace(".", "")
text09b = text09.split()
#print(text09b)
temp = ""
for txt in text09b:
    if len(txt) <= 4:
        pass
    else:
        txt = txt[0]+"".join(random.sample(txt[1:-1], len(txt[1:-1])))+txt[-1]
    temp += txt + " "
result = temp[:-1] + "."
print(result)