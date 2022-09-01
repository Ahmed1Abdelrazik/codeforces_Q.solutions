# Ahmed Abdelrazik
 
t = int(input())
for _ in range(t):
    n = int(input())
 
    if n%2 !=0 or n == 2: print(-1)
 
    else:
        N = n//2
        if N%2==0 and N%3 ==0:
            print(N//3,N//2)
        elif N%2 ==0:
            print(N//3+1,N//2)
        elif N%3 ==0:
            print(N//3, N//2)
        else:
            print(N//3+1,N//2)