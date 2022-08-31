n = int(input())
result = 0
for i in range(n):
    A = input().split(" ")
 
    if int(A[0])+int(A[1])+int(A[2]) >= 2:
        result +=1
print(result)
