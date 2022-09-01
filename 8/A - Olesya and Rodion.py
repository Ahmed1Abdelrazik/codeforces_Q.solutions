# Ahmed_Abdelrazik
a,b = map(int,input().split())
 
if a == 1 and b ==10:
    print(-1)
elif b ==10 and a !=1:
    print("1"+"0"*(a-1))
else:
    print(str(b)*a)
 