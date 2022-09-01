#Ahmed Abdelrazik
 
for _ in range(int(input())):
    A = list(map(int,input().split()))
    n = len(A)
    max1 = max(A)
    A1 = A.copy()
    A1.remove(max1)
    max2 = max(A1)
 
    in1 = A.index(max1)
    in2 = A.index(max2)
    if abs( in1 - in2) != 1: print("YES")
    else:
        print("NO" if min(in1, in2 )%2 == 0 else "YES")