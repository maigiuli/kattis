n = int(input())
r = [int(x) for x in input().split()]
print(r)
r2 = [x for x in r]
r2.sort(reverse=True)
print(r2)
count = [0 for _ in range(len(r))]
for i,r1 in enumerate(r2):
    print("index")
    index = r.index(r1)
    print(index)
    print(r2[i:])
    count[index]=len(r2[i:])-1
print(*count)