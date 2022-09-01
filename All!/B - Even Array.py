# Ahmed Abdelrazik
 
t = int(input())
 
for _ in range(t):
    odd = 0
    even =0
 
    n = int(input())
    a = list(map(int,input().split()))
 
    for i in range(n):
        if i%2 ==0:
            if a[i]%2 !=0 :
                even+=1
 
        else:
            if a[i]%2 !=1:
                odd +=1
 
    print(even if even == odd else -1)