#include <iostream>
#include <cmath>
using namespace std;
 
int main()
{
    int t;
    cin>>t;
    for(int i =0;i<t;i++){
        double n,x;
        cin>>n>>x;
        int f = ceil((n-2)/x);
        if(n<=2){
            cout<<1<<endl;
        }
        else{
            cout<<(f+1)<<endl;
        }
    }
 
    return 0;
}