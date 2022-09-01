 #include <bits/stdc++.h>
using namespace std;
 
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	int n;
    cin>>n;
    int res = 0;
    for(int i = 0 ; i<n;i++){
    	string word;
     	cin>>word;
     	if (word[1] =='+') res+=1;
 		else res-=1;
     }
     cout<<res;
	return 0;
}
