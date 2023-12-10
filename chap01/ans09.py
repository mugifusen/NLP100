import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"
word_list = []
result_list = []
words = s.split()
for word in words:
    word_list.append(word)
#print(word_list)

new_list = []
new_list = word_list[1:-1]
#print(new_list)
#["couldn't", 'believe', 'that', 'I', 'could', 'actually', 'understand', 'what', 'I', 'was', 'reading', ':', 'the', 'phenomenal', 'power', 'of', 'the', 'human']

random.shuffle(new_list)
#print(new_list)
print(word_list[0])
print(new_list)
print(word_list[-1])