# Ahmed_Abdelrazik
 
 
t = int(input())
 
for i in range(t):
    n= int(input())
    integers = list(map(int,input().split()))
    if n ==1:
        print("YES")
    else:
        if integers[n-1] - integers[0] > n+1:
            print("NO")
        else:
            print("YES")