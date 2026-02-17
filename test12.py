
#BABY BITES

n = int(input())
arild = input().split(' ')

ideal = [str(i+1) for i in range(n)]
print(ideal)
current = 0
for i, a in zip(ideal, arild):  
    if i==a: 
        print(i, "equal to ", a)
        current = current + 1 
        continue 
    if i!=a and a=="mumble": 
        arild[current] = str(int(i))
    current = current + 1 


print(arild)

result = "makes sense"
for i, a in zip(ideal, arild):  
    if i!=a: 
        result = "something fishy"
    
print(result)


