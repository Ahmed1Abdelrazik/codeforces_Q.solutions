#Ahmed Abdelrazik
n,m = map(int,input().split())
k = False
for _ in range(n):
        L = list(map(str,input().split()))
        if k == False:
            if "C" in L or "M" in L or "Y" in L:
                k = True
                print("#Color")
                break
 
if k == False:
    print("#Black&White")