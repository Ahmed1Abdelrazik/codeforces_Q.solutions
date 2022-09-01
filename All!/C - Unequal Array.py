#Ahmed_Abdelrazik
 
t = int(input())
 
for q in range(t):
    n =int(input())
    W = list(map(int,input().split()))
 
    in0 = 0
    inl = 0
    total = []
    out =0
    for i in range(n-1):
        if W[i] == W[i+1]:
            in0 = i
            break
    for i in range(n-1):
        if W[n-i-1] == W[n-i-2] :
            inl = n-i-1
            break
 
    if inl-in0 == 2:
        print(1)
    elif inl-in0>2:
        print(inl-in0-2)
    else:
        print(0)