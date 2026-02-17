
import math
n, t = map(int, input().split(' '))

#t time to drink potions 
t_i = [] 
effects = []
for i in range(n):
    t_i.append(int(input()))
    effects.append(False)

t_i.sort(reverse=True)

i = 0 
active = 0 

for time in range(t+t_i[0]+1):
    print("time" , time)
   
    if time<t: 
        print("Bevuta iniziale")
    else:
        active = round(time/t) -1 
        
        print("Sono attive", active, "effetti")
        
if (active==n):
    print("YES")
else:
    print("NO")
        

    

    


    
    
    