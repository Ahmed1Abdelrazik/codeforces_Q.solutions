#include <iostream>
 
using namespace std;
 
int main()
{
    int t;
    cin >>t;
 
    if(t%2 != 0)
        cout<<9<<" "<<t-9;
    else
        cout<<4<<" "<<t-4;
 
    return 0;
}