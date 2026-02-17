import math
n = int(input())

second = n % 60 

minutes = math.floor((n) / 60) %60

hours = round((round((n) / 60 )-minutes)/60)

print (str(hours) + " : " + str(minutes) + " : " + str(second))