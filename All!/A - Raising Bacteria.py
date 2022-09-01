from math import log2
def Bacteria(m):
    count = 0
    while m:
        if m ==1:
            count += 1
            break
        else:
            m -= 2 ** int(log2(m))
            count += 1
    print(count)
 
 
Bacteria(int(input()))