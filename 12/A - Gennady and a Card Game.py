#Ahmed Abdelrazik
 
def Check(S,List):
    S0, S1 = S[0], S[1]
    for K in List:
        if S0==K[0] or S1 ==K[1]:
            print("YES")
            break
    else:
        print("NO")
 
S = input()
List = list(map(str,input().split()))
Check(S,List)