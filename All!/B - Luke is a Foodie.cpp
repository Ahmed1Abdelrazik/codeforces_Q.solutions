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
 
#define for(i,n) for(int i = 0; i<n ; i++) 
#define For(i,a,n) for(int i = a; i<n ; i++) 
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
  		int n,x;
  		int count =0;
  		cin>>n>>x;
  		int a[n];
  		for(i,n){
  			cin>>a[i];
  		}
  	
  		int v0 = a[0]-x;
  		int v1 = a[0]+x;
 
  		for(i,n-1){
  			if(abs(a[i+1]-v1) <=x || abs(a[i+1]-v0)<=x ){
  				if(a[i+1] + x > v1 && a[i+1] - x < v0){
  					
  				}
  				else{
  				if(a[i+1] > a[i]){
  					v0 = a[i+1] - x;
  				}
  				else if(a[i+1] < a[i]){
  					v1 = a[i+1] +x;
  				}
  			}
  				continue;
  			}
  			else{
  				count++;
  				v0=a[i+1]-x;
  				v1=a[i+1]+x;
  			}
  		}
  		cout<<count<<"\n";
 
	}
 
  	return 0;
 
}