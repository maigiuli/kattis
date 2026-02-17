
#BABY SHARK

words = input()
words_separated = words.split(' ')
maximum = 0 
saved_word = ''

counts = []
for i, w in enumerate(words_separated): 
    if i==0:
        count = 1
        continue
    if i==(len(words_separated)-1):
        count+=1
        counts.append(count)
        continue
    
    if w==words_separated[i-1]:
        count+=1
        print("continuo a contare")
    else:
        print("smetto di contare")
        counts.append(count)
        count = 1
    print(count)


print(counts)
unique=0
for i, j in enumerate(counts): 
    if j == max(counts) and unique==0: 
        print(i)
        print(words_separated[i+1])
        unique=1
