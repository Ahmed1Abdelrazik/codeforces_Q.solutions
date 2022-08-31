#include <iostream>
using namespace std;
 
 
int main ()
{
 int Limak, Bob, counter;
 cin>>Limak>>Bob;
 
while(Limak <= Bob){
	Limak *= 3;
	Bob *= 2;
	counter ++;
	
}
 
 cout<<counter;
 
  return 0;
}