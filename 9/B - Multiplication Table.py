# Ahmed Abdelrazik
 
t= int(input())
original_array = []
Matris = []
 
while t:
    Matris.append(list(map(int,input().split())))  # i-row ,   j-column
    t-=1
 
original_array.append(str( int((Matris[1][0] * Matris[2][0]/Matris[2][1])**.5) ))
 
for i in range(1,len(Matris)):
    original_array.append(  str(  int( Matris[i][0]/int(original_array[0]) )  )   )
 
print(" ".join(original_array))
 