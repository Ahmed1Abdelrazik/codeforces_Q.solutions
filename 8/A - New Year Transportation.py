# Ahmed_Abdelrazik
 
n,t = map(int,input().split())
a = list(map(int,input().split()))
 
i = 1
flag = False
for _ in range(n):
    if i > n-1 :
        break
    if i+a[i-1] == t:
        flag = True
        print("YES")
    i = i + a[i-1]
if flag ==False:
    print("NO")