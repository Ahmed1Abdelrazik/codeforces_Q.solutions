#100 prob
q = int(input())
p = 0
E = [100,20,10,5,1]
while q>0:
    for r in E:
        if q//r != 0:
            p += q//r
            q = q%r
print(p)