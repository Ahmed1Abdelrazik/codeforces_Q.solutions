#Strings always win!
No = int(input())
W = list(map(int,input().split()))
 
for i in range(No):
    if i !=0 and i !=(No-1) :
        print(min(abs(W[i]-W[i-1]),abs(W[i]-W[i+1])),end = " ")
        print(max(abs(W[i]-W[No-1]),abs(W[i]-W[0])))
    if i ==0:
        print(abs(W[i]-W[i+1]),end = " ")
        print(abs(W[i]-W[No-1]))
 
    if i == (No-1):
        print(abs(W[i]-W[i-1]),end = " ")
        print(abs(W[i]-W[0]))
