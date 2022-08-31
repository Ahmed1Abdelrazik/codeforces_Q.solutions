E= input().split()
(Q,W) = (int(E[0]), int(E[1]))
n =0
for k in range(10):
    if ((Q%10) * (k+1))%10  == W:
        n = k+1
        break
if n >=1:
    print(n)
else:
    for i in range(10):
        if (Q%10 * (i+1))%10 ==0:
            print(i+1)
            break