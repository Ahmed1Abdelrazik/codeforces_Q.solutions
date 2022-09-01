# Ahmed Abdelrazik
 
n,a,b=map(int,input().split())
T = 0
 
for i in range(1,n+1):
    if n-i <=b and i-1 >=a:
        T+=1
 
print(T)