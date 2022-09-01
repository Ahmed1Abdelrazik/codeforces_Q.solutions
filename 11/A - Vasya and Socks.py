# Ahmed Abdelrazik
 
 
 
 
 
n,m = map(int,input().split())
sum = n
c = 0
while n > 0:
        sum  += n//m
        c    += n%m
        n    = n//m
        if c >= m:
                n += c
                c = 0
 
print(sum)