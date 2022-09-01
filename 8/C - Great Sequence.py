# Ahmed Abdelrazik
 
for i in range(int(input())):
    n,x = map(int,input().split())
    W = list(map(int,input().split()))
    Map1 = {}
    W.sort()
    for w in W:
        if w not in Map1:
            Map1[w] = 1
 
        else:
            Map1[w]+= 1
 
 
    for key in Map1:
        if Map1[key]!=0:
            if key/x in Map1 and Map1[key/x] !=0:
                m91 = min(Map1[key],Map1[key/x])
                Map1[key/x]-=m91
                Map1[key] -= m91
    Total91 =0
    for q in Map1:
        if Map1[q]!=0:
            Total91+=Map1[q]
 
 
 
    print(Total91)