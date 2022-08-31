### Strings always win!
L = list(map(int,input().split()))
(n, t ,k ,d) = (L[0],L[1],L[2],L[3])
if (n-(int(int(d/t))) * k )/ k >1 :
    print("YES")
else:
    print("NO")
