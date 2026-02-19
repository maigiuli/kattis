alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = input()
k = input()
new = ""
ind = 1
for i, j in zip(c,k):
    # i = C , j = A
    if ind%2==0:
        orig = alph.index(i)
        shift = alph.index(j) 
        new += alph[(orig+shift)%len(alph)]
    else: 
        ii = alph.index(i)-alph.index(j)
        new +=alph[ii]
    ind+=1
    
print(new)