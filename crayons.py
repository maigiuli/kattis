n, k = map(int, input().split())
r=0
for _ in range(n):
    s = [x for x in input().split()]
    ele = list(set(s))
    for i in ele:
        if s.count(i)>1:
            r+=s.count(i)-1
print(r)
        
        