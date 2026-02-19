dep, f = input().split()
f = int(f)
e=0
deps = {"residential":[2,6,11,16], "commercial":[2,8,15], "industrial":[2,5,9,13,17]}
if f==1:
    print(e)
else:
    i=1
    while i<=f:
        if i in deps[dep]: e+=1
        i+=1
    print(e)