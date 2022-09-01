# Ahmed Abdelrazik
 
for k in range(int(input())):
    n = int(input())
    W = list(map(int,input().split()))
    Wcopy = {}
    dis = 0
    for i in W:
        if i not in Wcopy:
            Wcopy[i] = True
            dis += 1
    for q in range(1, n+1):
        if q <= dis:
            print(dis,end=" ")
        else:
            print(q,  end=" ")
    print()