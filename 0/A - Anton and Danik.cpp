#include <iostream>
#include<ios>
#include<limits>
using namespace std;
#include <string>
int main ()
{
 int n, Anton=0, Danik = 0;
 string Word;
 cin>>n;
 cin.ignore(numeric_limits<streamsize>::max(), '\n');
 getline(cin,Word);
 
for(int i = 0; i<Word.length();i++){
	if(Word[i]=='A')
		Anton += 1;
	else
		Danik +=1;
}
 
if(Anton>Danik)
	cout<<"Anton";
else if(Danik > Anton)
	cout<<"Danik";
else
	cout<<"Friendship";
  return 0;
}