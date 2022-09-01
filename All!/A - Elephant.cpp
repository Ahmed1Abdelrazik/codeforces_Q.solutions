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
 
	if (n%5 ==0) cout<<n/5;
	else cout<<n/5 + 1;
 
	return 0;
}
