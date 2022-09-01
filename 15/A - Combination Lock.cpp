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
 
bool comp(int a , int b){
	return (a % 10) > (b% 10);
}
 
 
int main(){
 
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//start here
 
  	int n ; cin>>n;
  	string a,b; cin>>a>>b;
  	int res = 0;
  	for(int i =0 ; i<n; i++){
  		res += min(abs(a[i]-b[i]),10-abs(a[i]-b[i]));
  	}
  	cout<<res;
 
}
