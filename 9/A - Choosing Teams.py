# Ahmed Abdelrazik
 
n,k = map(int, input().split())
 
W = map(int,input().split())
 
son = 0
for q in W:
    if q+k <=5: son+=1
print(son//3)
