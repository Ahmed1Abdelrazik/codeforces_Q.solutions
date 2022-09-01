/*Ahmed Abdelrazik*/
 
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
#define append push_back
#define pair make_pair
#define search(vec,a) binary_search(vec.begin(), vec.end(), a)
const long long INF = 0x3f3f3f3f3f3f3f3f;
// #define for(i,n) for(int i = 0; i<n ; i++) 
// #define For(i,a,n) for(int i = a; i<n ; i++) 
int Search(double Sum, int n, vi v){
	vector<int>::iterator itr = find(v.begin(), v.end(), ceil(Sum/n));
	int index = distance(v.begin(), itr);
	return index;
}
ll F(int n){
	if(n==0) return 1;
	return n*F(n-1);
}
 
int main(){
 
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//start here
 
 	int a,b; cin>>a>>b;
 	if(a>b)cout<<F(b);
 	else cout<<F(a);
 
 
 
}