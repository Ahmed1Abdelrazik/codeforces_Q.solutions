#Abdelrazik
 
def Will_print(Q):
    W = ["H","Q","9"]
 
    for q in range(len(Q)):
        if Q[q] in W:
            return "YES"
 
    return "NO"
 
Q = input()
print(Will_print(Q))