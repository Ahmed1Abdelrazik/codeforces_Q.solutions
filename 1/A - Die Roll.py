Q= input().split()
n = max(int(Q[0]),int(Q[1]))
 
if n == 1:
    print(str(1) + "/" + str(1))
else:
    if (7-n)%2==0 or (7-n)%3==0 :
        if (7-n)==3:
            print(str(1) + "/" + str(2))
        else:
            print(str(int((7-n)/2)) + "/" + str(3))
    else:
        print(str(7-n) + "/" + str(6))