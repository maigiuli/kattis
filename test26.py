

numbers = [int(x) for x in input().split(' ')]

string = input()

output = []
a = min(numbers)
numbers.remove(a)
c = max(numbers)
numbers.remove(c)
b = numbers[0]

dictionary = {"A": a, "B": b, "C": c}

output = ""
for s in string:
    output += str(dictionary[s]) +" "
    
print(output)
    
    