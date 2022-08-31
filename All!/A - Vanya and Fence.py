 
 
A = input().split(" ")
B = input().split(" ")
 
 
n = int(A[0])    #number of students
h = int(A[1])    #Height of friends
result = 0
for i in B:
    if int(i) <= h:
        result += 1
    else:
        result += 2
 
print(result)
 
 
 
 