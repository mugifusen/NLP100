import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"
word_list = s.split()

new_list = word_list[1:-1]
for i in new_list:
    if len(i) < 4:
        pass        
    else:
        random.shuffle(new_list)

start = [word_list[0]]
end = [word_list[-1]]
result_list = start + new_list + end

print(result_list)