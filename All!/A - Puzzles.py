#Abdelrazik
 
n,m = map(int,input().split())
List = list(map(int,input().split()))
List.sort()
 
W = []
for i in range(m-n+1):
    W.append(List[n+i-1]-List[i])
 
print(min(W))