#Abdelrazik
 
def rooms_Check(n):
    count = 0
    for i in range(n):
        W = list(map(int,input().split()))
        if W[1]-W[0] >=2 :
            count += 1
 
    return  count
 
n = int(input())
print(rooms_Check(n))