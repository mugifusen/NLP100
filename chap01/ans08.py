# 答え見ました。
import re
def cipher(text):
    repatter = re.compile('[a-z]')
    temp = ""
    for ch in text:
        if re.match(repatter, ch):
            ch = chr(219 - ord(ch))
        temp += ch
    return temp

encode = cipher("I went to Ehime Prefecture yesterday")
print("暗号化:",encode)
decode = cipher(encode)
print("復号化:",decode)