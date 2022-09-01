# Ahmed Abdelrazik
n = int(input())
B = list(map(int,input().split()))
 
if n == 1:
    print(0)
else:
    while B[0]==B[1]:
        B.pop(0)
        if len(B)==1 :break
 
    T=0
    n = len(B)
 
    if n == 1:
        print(0)
    elif B[0] > B[1]:
        big = B[0]
        small= B[1]
        T =1
        for i in range(2,n):
            if B[i] > big:
                big = B[i]
                T+=1
            if B[i]<small:
                small = B[i]
                T +=1
        print(T)
 
    elif B[0] < B[1]:
        big = B[1]
        small= B[0]
        T = 1
        for i in range(2,n):
            if B[i] > big:
                big = B[i]
                T+=1
            if B[i]< small:
                small = B[i]
                T +=1
 
        print(T)
