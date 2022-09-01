#include <iostream>
#include <cmath>
using namespace std;
 
int main()
{
    int n,k;
    cin>>n>>k;
    k = 4*60 - k;
    float q = sqrt(.25 + .4 * k);
    int e = q - .5;
    cout<<fmin(e,n);
    return 0;
}