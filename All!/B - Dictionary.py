
# Ahmed Abdelrazik
Alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 
 
t = int(input())
for i in range(t):
    w = input()
    a = Alpha.index(w[0])
 
    if Alpha.index(w[1])>Alpha.index(w[0]):
        b= Alpha.index(w[1])
    else:
        b = Alpha.index(w[1]) +1
    print(a *25 + b)