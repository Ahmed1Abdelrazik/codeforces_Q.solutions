# Ahmed Abdelrazik
#by BinarySearch
import bisect
 
 
n = int(input())
Xi =sorted(map(int, input().split()))
 
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect.bisect_right(Xi,m))