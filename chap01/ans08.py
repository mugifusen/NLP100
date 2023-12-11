text = "Hello World"
 
def cipher(w):
    lis = []
    for i in w:
        if i.islower():
            i = chr(219 - ord(i))
        lis.append(i)
    return "".join(lis)
 
enc = cipher(text)
 
print(f"暗号化：{enc}")
print(f"復号化：{cipher(enc)}")