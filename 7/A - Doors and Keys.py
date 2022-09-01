#Ahmed_Abdelrazik
for i in range(int(input())):
    s = input()
    l = ["r","g","b"]
    L = ["R","G","B"]
    for q in range(3):
        if s.index(L[q]) < s.index(l[q]):
            print("NO")
            break
    else:
        print("YES")