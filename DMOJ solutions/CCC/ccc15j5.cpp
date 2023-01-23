#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int visited[251][251][251];

int pi(int n, int k, int min){
	if (visited[n][k][min]==0){
	
		if (n==k){
			visited[n][k][min]=1;
		}else if (k==1){
			visited[n][k][min]=1;
		}else{
			int t = 0;
			for(int i=min;i<=n/k;i++){
				t += pi(n-i,k-1,i);
			}
			visited[n][k][min] = t;
		}
    }
	return visited[n][k][min];
}


int main(void){
	int n,k;
	cin>>n>>k;
	for(int i=0;i<=n;i++){
		for(int j=0;j<=k;j++){
			for(int x=0;x<=n;x++){
				visited[i][j][x]=0;
			}
		}
	}
    //int visited[n+1][k+1][n+1];
	cout<<pi(n,k,1);
	
}