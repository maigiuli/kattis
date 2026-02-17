


def find_number(n):
    
    unit=0
    decine=0
    migliaia=0
    centinaia = 0
    decmigliaia=0
    for i in range(5):
        digit = (n // 10**i) % 10
        
        if i==0: unit=digit
        if i==1: decine=digit
        if i==2: centinaia=digit
        if i==3: migliaia=digit
        if i==4: decmigliaia=digit

    closest = 0 
    if n < 100:
        closest = 99
    else:
        if decmigliaia==0 and migliaia==0:
            option1 = centinaia*100+99
            option2 = (centinaia-1)*100+99
            closest_diff = option1-n if abs(option1-n) < abs(option2-n) else option2-n
            closest = closest_diff + n 
            if abs(option1-n) == abs(option2-n): closest = max(option1, option2)
        elif decmigliaia==0 and migliaia!=0:
            option1 = centinaia*100+99
            option2 = (migliaia)*1000+(centinaia-1)*100+99 #9899 
            option3 = (migliaia-1)*1000+centinaia*100+99  #8999
            option4 = (migliaia)*1000+centinaia*100+99    #9999
            closest_diff = n
            closest_i = 0
            options = [(option1-n), (option2-n), (option3-n), (option4-n)]


            for i,item in enumerate(options):
          
                if abs(item)<closest_diff:
                    closest_diff = abs(item)
                    closest_i = i 
            closest = options[closest_i] +n
            abs_array = [abs(i) for i in options]
            abs_array.sort()
            if abs_array[0]==abs_array[1]:
                closest = abs_array[1]+n


                
        else:
            closest = 9999


    print(str(n) + "   " +str(closest))
    return closest 

output = []
for i in range(10001):
    output.append(find_number(i))
    if output[i]!=output[i-1]:
        print("cambio!!!")
    
