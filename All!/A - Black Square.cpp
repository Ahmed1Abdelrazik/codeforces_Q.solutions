#include <iostream>
#include <sstream>
using namespace std;
#include<limits>
#include <string>
int main ()
{
 int Q[4],result,num;
 string W;
 for(int i=0; i<4; i++)
 	cin>>Q[i];
cin.ignore(numeric_limits<streamsize>::max(), '\n');
getline (cin,W);
 
for(int k = 0; k< W.length(); k ++){
	stringstream ss;  
  	ss << W[k];  
  	ss >> num;
	result += Q[num-1];
}
 
 
cout<<result;
  return 0;
}