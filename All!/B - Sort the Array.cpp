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
 
  	int n; cin>>n;
  	int a[n];
	for(int i= 0 ; i<n; ++i) cin>>a[i];
 
	bool ok = true;
	
	int index1=1;
	int index2=1;
 
	for(int i = 1; i<n ; i++){
		if(a[i]<a[i-1]){
			index1 = i;
			break;
		}
	}
	for(int i = n-1; i>0 ; i--){
		if(a[i]<a[i-1]){
			index2 = i+1;
			break;
		}
	}
	
	for(int i = index1; i< index2 ; i++){
		if(a[i]>a[i-1]){
			ok = false;
		}
	}
	if(index2<n){
		if( a[index1-1]> a[index2]  ) {
			ok=false;
		}
	}
    if(index1>1){ if (a[index1-2]>a[index2-1]) ok = false;} 
 
	if(ok==true) cout<<"yes\n"<<index1<<" "<<index2;
	else cout<<"no";
 
 
}
 
 
 
 