// #include <iostream>
#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int k;
    int count = 0;
    int d = 11;
    int sum=0;
    cin>>k;
    int a[12];
    
    for(int i = 0 ; i<12; i++){
        cin>>a[i];
        sum+= a[i];
    }
    sort(a, a + 12);
    // cout<<a[11];
    
    if (k<=sum){
    while(k>0){
        k-=a[d];
        d-=1;
        count += 1;
    }
    cout<<count;
    }
    else cout<<-1;
    return 0;
}