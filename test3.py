from collections import deque


r, c = input().split(' ')
mappa = []
for i in range(int(r)):
    row = input()
    mappa.append([int(x) for x in row])
    

    
dir = {"nord" : (-1,0), 
       "sud": (1,0),
        "est": (0,-1),
        "west": (0,1)}
print(mappa)
groups = []
for i in range(int(r)):
    for j in range(int(c)):
        
        type = mappa[i][j] 
        if type==2:
            continue
        group = []
        group.append([i,j])
        print("Testing cell ", i, " ", j )
        
        for key, x in dir.items():
            dr = x[0]
            dc = x[1]
            nr, nc = i + dr, j + dc
            if 0 <= nr < len(mappa) and 0 <= nc < len(mappa[0]):
                print("Testing step ", key, " at ", nr, " ", nc)
                print("type ", mappa[nr][nc])
                if mappa[nr][nc]==type:
                    print("same value: change number")
                    group.append([nr,nc])
                    mappa[nr][nc]=2
                    mappa[i][j]=2
            
        groups.append(group)        
print(groups)
print(mappa)

# vorrei: gruppo 1: [(0,0), (1,0), (2,0)] gruppo 2 [(0,1), (1,1), (2,1)]