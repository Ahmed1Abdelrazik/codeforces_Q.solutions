#Abdelrazik
First  = input()
Second = input()
 
XD     = First+Second
String = input()
 
flag  = True
if len(XD) == len(String):
    for i in XD:
        if XD.count(i) != String.count(i):
            print("NO")
            flag = False
            break
    if flag == True:
        print("YES")
else:
    print("NO")