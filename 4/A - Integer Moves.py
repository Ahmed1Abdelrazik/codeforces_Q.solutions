#Abdlerazik
 
n = int(input())
output= [0]*n
for i in range(n):
    pyth = list(map(int,input().split()))
    if pyth[0] ==0 and pyth[1]==0:
        output[i] = 0
    elif ((pyth[0]**2 +pyth[1]**2) **.5 ).is_integer() == True:
        output[i] = 1
    else:
        output[i] =2
    print(output[i])