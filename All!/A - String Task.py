#Abdelrazik
 
vouls =  ["a", "o", "y", "e", "u", "i"]
out = ""
 
for i in input().lower():
    if i not in vouls:
        out += "." + str(i)
print(out)
 