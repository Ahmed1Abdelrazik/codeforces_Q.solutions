# Ahmed Abdelrazik
Sum=0
for _ in range(int(input())):
        a,b,c = map(int,input().split())
        if (a+b)%c!=0:
                x,y,z = a+b+a*c,b+a*c,c
        else:   x,y,z = a+b+2*a*c, b+2*a*c,c
        print(x,y,z)