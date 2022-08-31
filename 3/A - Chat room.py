#Abdelrazik
 
def Checker(Txt):
    Hello = "hello"
    INDEXER = []
    n= 0
    for q in Txt:
        if n <5:
            if q == Hello[n]:
 
                INDEXER.append(Txt.index(q))
                n+=1
                Txt  = Txt[Txt.index(q):]
 
    if len(INDEXER) == 5:    return "YES"
    else:
         return "NO"
 
 
 
 
 
Txt = input()
print(Checker(Txt))