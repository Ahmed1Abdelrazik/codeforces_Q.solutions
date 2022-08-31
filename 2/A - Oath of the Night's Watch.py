#Abdelrazik
R = int(input())
Stewards = list(map(int,input().split()))
n= 0
 
n+= Stewards.count(max(Stewards))
 
n+= Stewards.count(min(Stewards))
 
if R >=2 and R>n:
    print(R-n)
else:
    print(0)