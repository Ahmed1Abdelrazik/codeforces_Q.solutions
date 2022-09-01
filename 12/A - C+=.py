#Ahmed Abdelrazik
 
for _ in range(int(input())):
        a,b,n = map(int,input().split())
        a0 = min(a,b)
        b0 = max(a,b)
        count0 = 0
        while a0<=n and b0<=n:
            a0+=b0
            count0+=1
            if a0>n: break
            else:
                b0 += a0
                count0 += 1
 
        print(count0)