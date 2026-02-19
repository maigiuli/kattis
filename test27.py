
import itertools

n = int(input())

languages = [int(i) for i in input().split(' ')]


min_min_diff = n 
for lang in languages: 
    indexes = [i for i, v in enumerate(languages) if v == lang]
    print(indexes)
    if len(indexes)>1:
        min_diff = min(abs(b - a) for p in itertools.permutations(indexes) for a,b in zip(p, p[1:])) 
        
        if min_diff < min_min_diff: 
         min_min_diff = min_diff
    else: 
        min_diff = 0
    
    print(min_min_diff)
        


print(min_min_diff)