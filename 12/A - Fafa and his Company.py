#Ahmed Abdelrazik
n = int(input())
i = 1
C = 0
while i<n:
    if (n-i) % i == 0: C+=1
    i+=1
 
print(C)