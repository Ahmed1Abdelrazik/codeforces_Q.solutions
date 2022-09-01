#Ahmed Abdelrazik
 
for _ in range(int(input())):
    a,b = map(int,input().split())
    while a>0 or b>0:
        if a>0:
            a-=1
            print(0,end="")
        if b>0:
            b-=1
            print(1, end="")
 
    print()