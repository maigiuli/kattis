
n = int(input())

strings=[]
for i in range(n):
    strings.append(input())
 
best_names = []
for item in strings: 
    if len(item)<5:
        continue
    for i in item: 
        count = item.count(i)
        if count!=1:
            break
    if count==1: 
        best_names.append(item)
    

result = sorted(best_names, key=lambda s: (len(s), s))

if len(best_names)==0: 
    print("Neibb")
else: 
    print(result[0])
 # 5 characthers
 #no repeated letter