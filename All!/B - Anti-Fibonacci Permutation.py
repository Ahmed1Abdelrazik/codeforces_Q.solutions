#Ahmed_Abdelrazik
t = int(input())
while t>0:
    n= int(input())
    S=[]
    for q in range(1,n+1):
        S.append(str(n+1-q)+" ")
    S*=2
    if n >3:
        for i in range(0,n):
            print("".join(S[i:i+n]))
    else:
        print(1,3,2)
        print(3,1,2)
        print(3,2,1)
    t-=1