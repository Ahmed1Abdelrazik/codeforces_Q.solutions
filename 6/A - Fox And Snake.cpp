#include <iostream>
using namespace std;
 
int main()
{
    int n,m=0;
    char x = '#',y='.';
    cin>>n>>m;
    for(int i = 0; i<n/2;++i){
            if(i%2 == 0){
        cout<<string(m, x)<<endl;
        cout<<string(m-1, y)<<x<<endl;
            }
            else{
        cout<<string(m, x)<<endl;
        cout<<x<<string(m-1, y)<<endl;
            }
    }
    cout<<string(m, x);
 
    return 0;
}
