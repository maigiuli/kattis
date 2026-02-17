
#BABYLONIAN NUMBERS

n = int(input())


for case in range(n): 
    sexagesimal = ""
    inp = input()
    if "," in inp: 
        sexagesimal = inp.split(",")
      
    else: 
        sexagesimal = [inp]
        
        
    decimal = 0 
    
    for i, d in enumerate(sexagesimal): 
        if d=="": d=0
        
        decimal += int(d) * 60**(len(sexagesimal)-1-i)
     
    print(decimal)