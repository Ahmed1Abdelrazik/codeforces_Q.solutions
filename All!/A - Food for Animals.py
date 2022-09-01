# Ahmed Abdelrazik
t = int(input())
 
for i in range(t):
    a,b,c,x,y = map(int,input().split())
 
    if a<=x:
        x -= a
    else:
        x = 0
    if b<=y:
        y -= b
    else:
        y =0
 
    remain = x+y-c
    if remain>0:
        print("NO")
    else:
        print("YES")