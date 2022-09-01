#Ahmed_Abdelrazik
 
t = int(input())
 
for i in range(t):
    n,m = map(int,input().split())
    if n==m:
        print(2*(n-1))
    elif n == 1 and m >=3:
        print(-1)
    elif m == 1 and n >= 3:
        print(-1)
    else:
        if (n>m):
            if (n-m) %2 ==0 :
                print(2*m-2+ 2*(n-m))
            else:
                print(2 * m - 2 + 2 * (n - m) -1)
 
 
        else:
            if (m-n) %2 ==0:
                print(2*n-2+ 2*(m-n))
            else:
                print(2 * n - 2 + 2 * (m - n) -1)