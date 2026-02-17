

#WHICH NUMBER IS THIS 

t = int(input())

for i in range(t):
    n = int(input())
    o = False 
    os = False 
    if n%2!=0:

        o=True

    if (n**0.5-round(n**0.5))==0:
        os = True
    if o ==True and os ==True: 
        print("OS")
    elif o ==True and os ==False: 
        print("O")
    elif o ==False and os ==True: 
        print("S")
    else: 
        print("EMPTY")