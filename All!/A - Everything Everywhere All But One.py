#Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    S = sum(A)
 
    for i in range(n):
        if (S -A[i])/(n-1) == A[i]:
            print("YES")
            break
    else:
        print("NO")
 
    # print("YES" if (sum(A)-orta)/(n-1) == orta else "NO")
 