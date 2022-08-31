#Abdelrazik
R = int(input())
W = list(map(int,input().split()))
W.sort(reverse= True)
Sum = 0
for k in W:
    Sum += k
Min = 0
NUM = 0
for i in W:
    if NUM<= Sum //2:
        NUM += i
        Min += 1
print(Min)