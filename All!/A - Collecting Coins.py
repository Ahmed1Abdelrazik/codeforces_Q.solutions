#Ahmed Abdelrazik
 
for _ in range(int(input())):
    a,b,c,n = map(int,input().split())
 
    print("YES" if n>=(3*max(a,b,c)-a-b-c) and (n- (3*max(a,b,c)-a-b-c)) %3==0
          else"NO")