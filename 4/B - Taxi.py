#Abdelrazik
 
def Taxi(n):
    W = list(map(int,input().split()))
    four = W.count(4)
    three = W.count(3)
    two = W.count(2)
    one = W.count(1)
    three_one = k =  min(three,one)
    three -= k
    one -= k
    if one %2 ==0:
        two_one = l =  min(two,one//2)
        two -= l
        one -= 2*l
    else:
        two_one = l =  min(two,one//2)
        two -= l
        one = one - 2*l + 1
    if one % 4 ==0:
        if two % 2 ==0:
            return int( four + three_one + two_one + three + one//4 + two /2 )
        else:
            return int( four + three_one + two_one + three + one // 4 + two // 2 +1 )
    else:
        if two % 2 == 0:
            return int(four + three_one + two_one + three + one // 4 +  1  + two / 2)
        else:
            return int( four + three_one + two_one + three + one // 4 + two // 2 +1 )
 
 
 
n = int(input())
 
print(Taxi(n))