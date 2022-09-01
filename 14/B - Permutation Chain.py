t = int(input())
for i in range(t):
    n = int(input())
    a = []
    print(n)
    for k in range(1, n + 1):
        a.append(str(k))
 
    j = 0
    while (j < n-1):
        print(" ".join(a))
        a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
 
    print(" ".join(a))