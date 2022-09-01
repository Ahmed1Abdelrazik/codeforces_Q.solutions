#include <bits/stdc++.h>
using namespace std;
#include <string>
int main()
{
    int t;
    cin>>t;
    
    for(int i= 0 ; i<t; i++){
        string W;
        int A=0;
        int B=0;
        int C=0;
        cin>>W;
        for(int j= 0 ; j<W.length(); j++){
 
            if (W[j]=='A') A+=1;
            if (W[j]=='B') B+=1;
            if (W[j]=='C') C+=1;
        }
        
        if(A+C==B) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}