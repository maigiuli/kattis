from itertools import groupby

n = int(input())
o=1
mapp = []
for _ in range(n): 
    r = input()
    mapp.append(r)
    
for i in range(n):
    if mapp[i].count("W")!=mapp[i].count("B"): 
        o=0
        break
    if mapp[:][i].count("W")!=mapp[:][i].count("B"): 
        o=0
        break
    col = ""
    for j in range(n):
        col += mapp[j][i]
    
    for s in ["W", "B"]:
        
        con = [len(list(v)) for k,v in groupby(mapp[i]) if k==s]
        con2 = [len(list(v)) for k,v in groupby(col) if k==s]
        for c in range(3,n):
            if c in con or c in con2: o=0 
        
    
    
print(o)