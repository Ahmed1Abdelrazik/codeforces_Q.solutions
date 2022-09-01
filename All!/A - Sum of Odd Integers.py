# Ahmed Abdelrazik
for _ in range(int(input())):
    n,k = map(int,input().split())
    C= (n%2==0 and k%2==0 and k**2<=n) or (n%2 !=0 and k%2!=0 and k**2<=n)
    print("YES" if C else "NO")