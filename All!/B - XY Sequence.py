#Abdlerazik
 
 
def XY_Sequence(n):
 
    for i in range(n):
        inputs = list(map(int, input().split()))   ## [0] = n,   <= [1] , x =[2], y =[3]
        Sq = [0]*(inputs[0]+1)
 
        for q in range(inputs[0]):
            if Sq[q] + inputs[2] <= inputs[1]:
                Sq[q+1] = Sq[q] + inputs[2]
            else:
                Sq[q+1] = Sq[q] - inputs[3]
        print(sum(Sq))
 
 
 
 
n = int(input())
XY_Sequence(n)