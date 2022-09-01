#include <cmath>
#include <bits/stdc++.h>
using namespace std;
 
int binomialCoeff(int n, int k)
{
 
    if (k > n)
        return 0;
    if (k == 0 || k == n)
        return 1;
 
    return binomialCoeff(n - 1, k - 1)
           + binomialCoeff(n - 1, k);
}
int main() 
{
  int n;
  cin >> n;
 
  cout << binomialCoeff(n*2-2,n-1);
  return 0;
}
