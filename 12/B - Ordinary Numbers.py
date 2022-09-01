#Ahmed Abdelrazik
import bisect
G = []
for i in range(1,10):
    for j in range(1,10):
        G.append(int(str(i)*j))
G.sort()
#print(G)
t = int(input())
 
while t>0:
    t-=1
    n = int(input())
    print(bisect.bisect_right(G,n))