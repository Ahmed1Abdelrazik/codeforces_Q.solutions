# Ahmed Abdelrazik
for _ in range(int(input())):
    a,b,n,S = map(int,input().split())
    C= (S//n <=a and S%n <=b) or (S-a*n >0 and S-a*n <=b)
    print("YES" if C else "NO")