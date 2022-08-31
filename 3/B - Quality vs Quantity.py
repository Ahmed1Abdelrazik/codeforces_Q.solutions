#Abdelrazik
q = int(input())
 
for i in range(q):
    p = int(input())
    Set_ = list(map(int,input().split()))
    Set_.sort(reverse= True)
 
    Sum1 = 0
    Sum2 = Set_[p-1]
    o = 0
    for i in range(int(p/2)):
        Sum1 += Set_[i]
        Sum2 += Set_[p-i-2]
 
        if Sum1 > Sum2:
            print("Yes")
            o = 1
            break
        else:
            continue
    if o == 0 :
        print("No")