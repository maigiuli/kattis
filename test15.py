

#GETTING WOOD 

t = input().split()
index = 0
for i, tree in enumerate(t): 
    if tree=="tree":
        index = i 

if index==0: 
    print("no trees here")
else: 
    print(index)
