#Ahmed_Abdelrazik
 
t = int(input())
 
for i in range(t):
    a,b = list(map(int,input().split()))
    if min(a,b)*2 >= max(a,b):
        print((min(a,b)*2)**2)
    else:
        print(max(a,b)**2)