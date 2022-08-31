#Abdelrazik
X = list(map(int,input().split()))
Sum = max(X)
X.remove(Sum)
print( Sum-X[0] ,Sum-X[1] ,Sum-X[2] )