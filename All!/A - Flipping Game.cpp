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
 
 
int C(int a[], int n, int i , int j ){
	int Z = 0;
	for(int r = i ; r< j ; r++){
 		 if(a[r] ==  0)Z++;
 		 else Z--;
 	}
 	return Z;
}
 
int main(){
 	
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
 	int n ; cin>>n;
 
 	int a[n];
 	int Z = n;
 	int O = 0;
 	for(int r = 0 ; r< n ; r++){
 		cin>>a[r];
 		 if(a[r] ==  1){O++; Z--;}
 	}
 	// cout<<C(a,n,0,n)<<endl;
 
 
	int max = -1;
 	for(int i = 0 ; i<n  ; i++){
 		for(int j =i+1 ; j<=n; j++){
 			int fun = C(a,n,i,j);
 			if (fun>max) max = fun;
 		}
 	}
 
 	cout<<O + max;
 
 		
}