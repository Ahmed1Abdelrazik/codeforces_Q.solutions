# Ahmed_Abdelrazik
 
 
t = int(input())
 
for i in range(t):
    s = input()
    #5 cases
    A = s.split("b")
    B = s.split("a")
    #print(A)
    #print(B)
    flag = True
    for a in A:
        if len(a)<2 and a!="":
            print("NO")
            flag=False
            break
    if flag == True:
        for b in B:
            if len(b)<2 and b!="":
                print("No")
                flag = False
                break
    if flag == True:
        print("YES")