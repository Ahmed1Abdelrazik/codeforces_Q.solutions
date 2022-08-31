#Abdelrazik
 
def String(n):
 
 
    for i in range(n):
        txt = input()
        for k in range(len(txt)):
            if txt[k] not in txt[k+1:]:
                print(txt[k:])
                break
 
 
n = int(input())
 
String(n)