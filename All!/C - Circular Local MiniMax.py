# Ahmed Abdelrazik
from collections import Counter
def Most_Common(List):
    data = Counter(List)
    Most = data.most_common(1)[0][0]
    return Most, List.count(Most)
 
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
 
    if n%2==1: print("NO")
    else:
        Most, count= Most_Common(A)
 
        if count <= (n/2):
            A = sorted(A)
            A1 = A[:n//2]
            A2 = A[n//2:]
            if Most in A1 and Most in A2 and count == n/2:
                print("NO")
            else:
                print("YES")
                for i in range(n // 2):
                    print(A1[i], A2[i], end=" ")
            print()
        else:
            print("NO")