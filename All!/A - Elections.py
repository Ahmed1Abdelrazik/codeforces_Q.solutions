# Ahmed Abdelrazik
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    F = [a,b,c]
    M =max(a,b,c)
    print(M-a+1 if a<M else (1 if F.count(a)>1 else 0),
          M-b+1 if b<M else(1 if F.count(b)>1 else 0),
          M-c+1 if c<M else(1 if F.count(c)>1 else 0 ))