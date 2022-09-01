/*Ahmed Abdelrazik*/
 
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
#define append push_back
#define pair make_pair
#define search(vec,a) binary_search(vec.begin(), vec.end(), a)
const ll INF = 0x3f3f3f3f3f3f3f3f;
// #define for(i,n) for(int i = 0; i<n ; i++) 
// #define For(i,a,n) for(int i = a; i<n ; i++) 
 
 
int main(){
 
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
 
 	int t; cin>>t;
 
 	while(t--){
 		int n; cin>>n;
 		int a[n];
 		for(int j = 0 ; j<n ; j++){
 			cin>>a[j];
 		}
 		int sizee =(1e5) * 2 +1; 
 		int count = 0;
 		int L[sizee]={0};
 		int maxx = 0;
 		for(int j = 0 ; j< n ; j++){
 			L[a[j]]++;
 			if ((L[a[j]])==1) count++; 
 			if (L[a[j]]>maxx) maxx = L[a[j]];
 		}
 
 		if(maxx > count)
 		cout<<count<<"\n";
 		else if(maxx == count)
 		cout<<maxx-1<<"\n";
 		
 		else
 			cout<<maxx <<"\n";
 
 
 	}
 		
}
 