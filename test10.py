
#BABY PANDA


# N number of days 
#EACH DAY: 0 / 1 slimes 
# EACH NIGHT: slimes double 
#M number of slimes after night N 

#numero di slimes alla fine =10 = [sl1*2^10 + (sl2+sl1)*2^9 + ...]
#numero di giorni = 10 

nm = input().split(' ')
n= int(nm[0])
m= int(nm[1])

added = []
while m> 0: 
    day_before = m/2
    if day_before%2==0:
        added.append(0)
        m = m/2
    else:
        added.append(1)
        m =m/2-1

print(sum(added))
  




1000000000000000000
