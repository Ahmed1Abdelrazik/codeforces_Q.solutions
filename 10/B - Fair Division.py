# Ahmed Abdelrazik
 
for _ in range(int(input())):
    n = int(input())
    A = map(int,input().split())
 
    one = 0
    two = 0
    for j in A:
        if j ==1: one+=1
        else: two +=1
 
 
    print("YES" if one%2 ==0 and one !=0
          else("Yes" if one ==0 and two%2==0 else"NO"))