# Ahmed Abdelrazik
#The Power Of FORMULA!
 
for _ in range(int(input())):
    n,k = map(int,input().split())
    e = 0
    if k%(n-1) == 0: e = -1
    else: e = k%(n-1)
    print( e + n*(k//(n-1)) )