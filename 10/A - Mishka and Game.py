# Ahmed Abdelrazik
M=0
N=0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a>b  : M+=1
    elif b>a:N+=1
print("Mishka" if M>N else("Chris"if N>M  else "Friendship is magic!^^"  ))