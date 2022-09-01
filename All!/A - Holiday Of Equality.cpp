#include <iostream>
using namespace std;
 
int main()
{
    int n,m=0;
    cin >>n;
    int t[n];
 
    for(int i = 0; i<n;++i){
        cin>>t[i];
        if(t[i]>m)
            m = t[i];
 
    }
    int c;
        for(int i = 0; i<n;++i){
        c += m- t[i];
        }
        cout<<c;
    return 0;
}