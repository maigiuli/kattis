n = int(input())



gifts = [0 for _ in range(n+1)] 
for j in range(1,n+1):
    i=j
    while i>0:
        gifts[j]+=i
        i-=1

print(gifts[-1])
print(sum(gifts))