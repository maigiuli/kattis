
n1 = input()
n2 = input()

n1= n1[::-1]
n2= n2[::-1]
if len(n1)>len(n2):
    for i in range(abs(len(n1)-len(n2))):
        n2+=" "
while len(n1)<len(n2):
    for i in range(abs(len(n2)-len(n1))):
        n1+=" "
    
    
winner_i = ""
winner_j = ""



for i, j in zip(n1, n2):
    if i=="":
        winner_i= i 
    if j=="":
        winner_j =j
        continue
    if(i>j):
        winner_i += str(i)
    elif(i==j):
        winner_i += str(i)
        winner_j += str(i)
    else: 
        winner_j += str(j)

if winner_i=="":
    winner_i="YODA"
elif winner_i.count("0")==len(winner_i):
    winner_i = "0"
else: 
    winner_i=winner_i[::-1]

if winner_j=="":
    winner_j="YODA"
elif winner_j.count("0")==len(winner_j):
    winner_j = "0"
else: 
    winner_j=winner_j[::-1]

print(winner_i)
print(winner_j)
    
