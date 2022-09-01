# Ahmed Abdelrazik
 
for k in range(int(input())):
    n = int(input())
    W = list(map(int,input().split()))
    Sum = sum(W)
    print( (n-Sum%n)*(Sum%n) )