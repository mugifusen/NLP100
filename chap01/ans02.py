string1 = "パトカー"
string2 = "タクシー"
result = ''

for char1, char2 in zip(string1, string2):
    result += char1 + char2
    #print(result)

print(result)