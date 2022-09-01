#Ahmed Abdelrazik
 
t = int(input())
 
while t>0:
    t-=1
    a,b = map(int,input().split())
    if a==b: print(0)
    if a>b:print(1 if (a-b) %2 ==0 else 2)
    if a<b:print(1 if (b-a) %2 ==1 else 2)