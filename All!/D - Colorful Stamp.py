#Abdelrazik
 
def neigbor(string):
    Dic = {}
    Dic["B"] = 0
    Dic["R"] = 0
    if string!="":
        for i in string:
            if i == "R":
                Dic["R"] +=1
            if i =='B':
                Dic["B"] +=1
        if Dic["B"] ==0 or Dic["R"] ==0:
            return False
        else:
            return True
 
t = int(input())
for i in range(t):
    n = int(input())
    S = input()
 
    Array = S.split("W")
    for word in Array:
        if neigbor(word) == False:
            print("NO")
            break
    else:
        print("YES")