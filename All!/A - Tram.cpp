#include <bits/stdc++.h>
using namespace std;
// #include <cctype>
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	int n;
	cin>>n;
	int a[n];
	for(int i =0; i<n; i++){
		int in,out;
		cin>>out>>in;
		a[i]= in-out;
}
	for(int i =1; i<n; i++){
			a[i] += a[i-1];
}
 
 
	cout<<*max_element(a , a + n);
	
 
	return 0;
}