# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    List = []
 
    for i in range(n):
        if A[i]!=i:
            List.append(i)
    result = List[0]&List[1]
    for k in range(len(List)):
        result = result&List[k]
    print(result)
 