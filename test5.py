
import math

def find_tempo(n):

    current = n
    i_saved = 0

    if n==1: 
        print(1)
    elif n==2:
        print(2)
    else:
        for i in range(n):
            
            #print("n", n)
            #print("i+1", i+1)
            #print(math.ceil(n/(i+1)))
            #print("i" + str(i+math.ceil(n/(2**i))))
            #print(current)
            #print("-----------")
            if (i+math.ceil(n/(i+1)))<current:
                current = i+math.ceil(n/(2**i))
                i_saved = i 
                

        print(n, "  ", current)
    


for i in range(70):
    find_tempo(i)

