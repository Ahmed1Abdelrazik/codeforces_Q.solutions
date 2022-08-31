#Abdelrazik
[k,n,w] = list(map(int,input().split()))
if int((k * (w*(w+1)/2))-n)>0:
    print(int((k * (w*(w+1)/2))-n))
else:
    print(0)