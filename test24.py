n, k = map(int,input().split(' '))


a = [int(x) for x in input().split(' ')]

output = ""
for i in range(n):
    if a[i]<=k:
        output += "1"
        k = k-a[i]
    else:
        output += "0"
    print(k)
        
print(output)
    