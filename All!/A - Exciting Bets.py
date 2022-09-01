#Ahmed_Abdelrazik
 
for k in range(int(input())):
    a,b = map(int,input().split())
    fark = abs(a-b)
    if a == b:
        print(0,0)
    else:
        print(fark,min(a%fark,fark - a%fark))