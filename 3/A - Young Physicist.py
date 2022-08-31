#Abdelrazik
Sum=[0,0,0]
for q in range(int(input())):
    List =  list(map(int,input().split()))
    Sum[0] += List[0]
    Sum[1] += List[1]
    Sum[2] += List[2]
if Sum == [0,0,0]:
    print("YES")
else:
    print("NO")
 