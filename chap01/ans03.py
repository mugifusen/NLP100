s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = s.replace(",", "").replace(".","").split()#,.をどける
lengths = []

for i in words:
    count = len(i)
    lengths.append(count)

print(lengths)
