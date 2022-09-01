# Ahmed Abdelrazik
 
for _ in range(int(input())):
        n = input()
        if len(n)==2:
                print(n[1])
        else:
                M = 465312
                for q in n:
                        if int(q)<M: M=int(q)
                print(M)