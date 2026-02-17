def contains(nested, target):
    for item in nested:
        if item == target:
            return True
        if isinstance(item, list) and contains(item, target):
            return True
    return False


n, d = map(int,input().split(' '))
p = []
for i in range(n):
    p.append(int(input()))
p.sort()
groups = []

count = 0
i = 0 
while i < n: 
    count +=1
    start = p[i]
    i += 1
    while i < n and p[i] - start <= d:
        i += 1

        

print(count)
        
