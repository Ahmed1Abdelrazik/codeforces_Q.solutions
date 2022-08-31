#Strings always win!
No = int(input())
W = list(map(int,input().split()))
 
The_list = ['']*No
 
for i in range(No):
    The_list[i] = W.index(i+1) +1
 
for T in range(No):
    print(The_list[T],end=' ')