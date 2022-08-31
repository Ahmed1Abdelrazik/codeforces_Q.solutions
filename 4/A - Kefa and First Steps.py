#Abdelrazik
 
def First_dp(n):
    W = list(map(int,input().split()))
    A = []
    count = 1
    for i in range(n-1):
        if W[i]<=W[i+1]:
            count += 1
        else:
            A.append(count)
            count= 1
    A.append(count)
    return max(A)
 
 
 
n = int(input())
 
print(First_dp(n))