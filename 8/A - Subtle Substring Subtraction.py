# Ahmed_Abdelrazik
 
Alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 
 
t = int(input())
 
for q in range(t):
    string = input()
    if len(string)==1:
        print("Bob",Alpha.index(string)+1)
    else:
 
        Total = []
        for s in string:
            Total.append(Alpha.index(s) + 1)
        if len(string)%2!=0:
            Min = min(Total[0],Total[-1])
            print("Alice",sum(Total)-2*Min)
        else:
            print("Alice",sum(Total))
        #print(Total)