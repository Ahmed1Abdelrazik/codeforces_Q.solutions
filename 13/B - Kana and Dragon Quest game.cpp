#include <bits/stdc++.h>
using namespace std;
 
 
int main()
{
    int t;
    int f = 0;
    cin>>t;
    
    
    for(int i =0 ; i <t; i++ ){
        int x,n,m;
        int f = 0;
        cin>>x>>n>>m;
        
        if(x <= 10*m ){
            cout<<"Yes"<<endl;
        }
        else{
        for(int j =0; j<n; j++){
            x/= 2;
            x+=10;
            if(x <= 10*m ){
                cout<<"Yes"<<endl;
                f=1;
                break;
        }
 
        
    }
 
    if (f==0) cout<<"No"<<endl;
    }
    }
    return 0;
}