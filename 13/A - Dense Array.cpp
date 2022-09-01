#include <bits/stdc++.h>
using namespace std;
#include <cmath>
#include <algorithm>
int main()
{
    int t;
    int count = 0;
    cin>>t;
    
    for(int i= 0 ; i<t; i++){
        int n;
        cin>>n;
        double a[n];
        for(int j=0; j<n;j++){
            cin>>a[j];
        }
        for(int r=0; r<n-1;r++){
            if (2*min(a[r],a[r+1])< max(a[r],a[r+1])){
                count += floor(log2(ceil((max(a[r],a[r+1])-min(a[r],a[r+1]))/min(a[r],a[r+1]))));   
 
    }
 
    }
            cout<<count<<endl;
            count = 0;
    }
    return 0;
}