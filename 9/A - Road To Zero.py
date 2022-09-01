# Ahmed Abdelrazik
 
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    if b <= 2*a:
        print( b*min(x,y) + a*(max(x,y)-min(x,y) ) )
    else:
        print(a*(x+y))