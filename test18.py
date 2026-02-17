

#CHICAGO CUBS 

n= int(input())

integers = [int(i) for i in input().split(' ')] #ATBATS 

walks = integers.count(-1)

sum = sum(integers)+walks
denominator = len(integers)-walks
print(sum/denominator)
