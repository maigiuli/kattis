from collections import deque



n, m, k = map(int, input().split())

tunnels = []
for i in range(n-1):
    tunnels.append([int(x) for x in input().split()])

racers = []
for i in range(m):
    racers.append([int(x) for x in input().split()])

end_checkpoint = int(input())
c = int(input())
specials = []
for i in range(c):
    specials.append(int(input()))




all_dist = []
for i in range(n):
    dist =[0 for _ in range(n)]
    all_dist.append(dist)


for i in range(1,n+1):
    for tunnel in tunnels: 
        if i in tunnel: 
            other = tunnel[0] if tunnel[0]!=i else tunnel[1]
            all_dist[i-1][other-1] = 1
            all_dist[other-1][i-1] = 1



print(all_dist)

dist = [-1] * n

q = deque()

dist[end_checkpoint-1] = 0
q.append(end_checkpoint-1)

# BFS
while q:
    u = q.popleft()
    for v in range(n):
        if all_dist[u][v] == 1 and dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

        
for i in range(n):
    print(f"dist[{i+1}] = {dist[i]}")



sorted(specials, key=lambda x: dist[x], reverse=True)
passed_special = [0 for _ in specials]

can_pass = [[True for _ in range(len(specials))] for _ in range(len(racers))]
vel_specials = [[0 for _ in range(n)] for _ in specials]
print(specials)

speeds = []
for racer in racers: 
    speeds.append(1/(racer[1]))
passing_per_special = [] 

for special in specials:
    arrivals = []

    for r_index, racer in enumerate(racers):
        start = racer[0]
        speed = 1/racer[1]

        if dist[special-1] < dist[start-1]:
            arrivals.append((speed, r_index)) 

    
    arrivals.sort(reverse=True)

    passing = [r_index for  _, r_index in arrivals[:k]]

    passing_per_special.append(passing)

print("special")
print(passing_per_special)

#per ogni special ho una lista di velocità che i giocatori hanno a quel punto 
times = []

for j, racer in enumerate(racers):
    eliminated = False
    print(j)
    for i, special in enumerate(specials):
        if dist[special-1] < dist[racer[0]-1]: 
            if j not in passing_per_special[i]:
                eliminated = True
    if eliminated:
        times.append(-1)
    else:
        times.append(racer[1] * dist[racer[0]-1])




print(times)
