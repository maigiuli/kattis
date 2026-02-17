n = int(input())
people = 0
max_people = 0 
for stop in range(n):
    a, b = map(int, input().split(' '))
    people = people + b-a 
   
    if people > max_people: 
        max_people = people 

print(max_people)