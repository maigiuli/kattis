
s = str(input())

original = "UAPC"
missing = ""
for letter in original: 
    if letter in s: 
        continue 
    else: 
        missing += letter
print(missing)