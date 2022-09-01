#Ahmed_Abdelrazik
 
t =int(input())
for i in range(t):
    S = input()
 
    if S[-1] !="A" and S[0] !="B":
        A = 0
        B = 0
        for i in S:
            if i == "A":
                A += 1
            else:
                B += 1
            if B > A:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")