

n, k = map(int, input().split(' '))

xs= [int(x) for x in input().split(' ')]

solution = []
for i in range(k-1,n,k):
    print(i)
    solution.append(xs[i])
        
ouptut = ""
for x in solution:
    ouptut+=str(x)+" "

print(ouptut)