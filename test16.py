

#CHANUKAH CHALLENGE

p = int(input())
for i in range(p):
    k, n = map(int, input().split(' '))
    n_candles = n+ sum([i+1 for i in range(n)])
    print(k, " ", n_candles)

#n = number of holiday 
