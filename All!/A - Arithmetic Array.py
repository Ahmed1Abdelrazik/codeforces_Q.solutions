# Ahmed Abdelrazik
for _ in range(int(input())):
    n = int(input())
    E = list(map(int,input().split()))
    F = sum(E)
    print(F-n if F-n>=0 else 1)