/*
	Ahmed_Abdelrazik
*/
 
#include <vector>
#include <iostream>
 
using namespace std;
 
int main()
{
	int n;
	cin >> n;
	int Mn=100, Mx=0,Mn_i=0,Mx_i=0;
	vector <int> v1(n);
 
	for (int i = 0; i < n; ++i) {
		cin >> v1[i];
		if (v1[i] > Mx) { Mx = v1[i]; }
		if (v1[i] < Mn) { Mn = v1[i]; }
	}
	for (int i = 0; i < n; ++i) {
		if (v1[n-i-1] == Mn) { Mn_i = n-i-1; break; }
	}
	for (int i = 0; i < n; ++i){
		if (v1[i] == Mx) { Mx_i = i; break; }
	}
	//cout << Mn << " " << Mx << endl;
	//cout << Mn_i << " " << Mx_i<<endl;
	if (Mn_i < Mx_i) {cout << n - Mn_i - 2 + Mx_i;}
	else {cout << n - Mn_i - 1 + Mx_i; }
	return 0;
}