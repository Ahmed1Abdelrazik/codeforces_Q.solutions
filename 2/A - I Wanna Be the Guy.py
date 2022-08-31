#Abdelrazik
n = int(input())
No1 = list(map(int,input().split()))
No2 = list(map(int,input().split()))
 
J = 1
 
for i in range(1,n+1):
    if i not in No1[1:] and i not in No2[1:]:
        print("Oh, my keyboard!")
        J = 0
        break
if J == 1 :
    print("I become the guy.")