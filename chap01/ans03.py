text1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text1_r = text1.replace(",", "").replace(".", "")
 
lis = []
for x in text1_r.split():
    lis.append(x)
    
len_l = [len(y) for y in lis]
print(len_l)