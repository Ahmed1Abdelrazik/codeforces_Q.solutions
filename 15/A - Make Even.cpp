/*Ahmed Abdelrazik*/
 
/*	vector<int>::iterator itr = find(v.begin(), v.end(), key);
	int index = distance(v.begin(), itr);
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
#define append push_back
#define pair make_pair
#define search(vec,a) binary_search(vec.begin(), vec.end(), a)
 
// #define for(i,n) for(int i = 0; i<n ; i++) 
// #define For(i,a,n) for(int i = a; i<n ; i++) 
int main(){
 
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//start here
 
  	
  	int t; cin>>t;
 
  	while(t--){
  		ll n; cin>>n;
  		string num = to_string(n);
  		bool f = false;
  		for(int i =0; i<num.length();i++){
  			if(num[i]%2 ==0) {f= true;break;}
  		}
  		if(n%2==0) cout<<"0\n";
  		else if(f==false) cout<<"-1\n";
  		else
  		cout<<((to_string(n)[0]%2 && f == true)? "2\n":"1\n");
 
  	}
 
 
  	return 0;
 
}