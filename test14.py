

#INTUITITVE ELEMENTS 

t = int(input())

for i in range(t):
    answer = "YES"
    a = str(input())
    b = str(input())

    for b_letter in b: 
        if a.find(b_letter)<0:
            answer = "NO"
            break
        else:
            continue 

    print(answer)
    
     
