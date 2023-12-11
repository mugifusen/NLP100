text1 = "パトカー"
text2 = "タクシー"
result = ''

lis = []
for x, y in zip(text1, text2):
    result += x + y

print(result)