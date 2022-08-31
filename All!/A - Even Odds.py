#Abdelrazik
No = list(map(int,input().split()))
n = No[0]
p = No[1]
 
if n%2 == 0:
    if p> n//2:
        print((p- (n//2)) *2)
    else:
        print(2*p-1)
 
else:
    if p> n//2 +1:
        print((p - (n // 2  +1)) * 2)
    else:
        print(2 * p - 1)
