#include <iostream>
#include <bits/stdc++.h>
#include <queue>
#include <vector>

using namespace std;

int main(){
	int N, M, L, A, B,node,n,dist,d;
	cin>>N>>M;
	//int distance[N+1];
	int big = 1000000000;
	vector<list<pair<int,int>>> paths(N);
	for(int i=0;i<M;i++){
		cin>>A>>B>>L;
		paths[A-1].push_back(make_pair(B-1,L));
	}
	int distance[N][2];
	bool poop[N] = {};
	for(int i = 0;i<N;i++){
		distance[i][0] = big;
		distance[i][1] = big;
	}
	distance[0][0] = 0; 
	queue<int>que;
	que.push(0);
	while(!que.empty()){
		node = que.front();
		que.pop();
		poop[node] = false;
		for(pair<int,int>path:paths[node]){
			n = path.first;
			d = path.second;
			if(distance[node][0]+d<distance[n][0]){
				distance[n][1] = distance[n][0];
				distance[n][0]=distance[node][0]+d;
				if(!poop[n]){
					que.push(n);
					poop[n]=true;
				}
			}
			else if(distance[node][0]+d<distance[n][1] && distance[node][0]+d!=distance[n][0]){
				distance[n][1] = distance[node][0]+d;
				if(!poop[n]){
					que.push(n);
					poop[n]=true;
				}
			}
			if(distance[node][1]+d<distance[n][1]&&distance[node][1]!=distance[n][0]){
				distance[n][1] = distance[node][1]+d;
				if(!poop[n]){
					que.push(n);
					poop[n] = true;
				}
			}
		}
	}
	if(distance[N-1][1]==big){
		cout<<-1;
	}else{
		cout<<distance[N-1][1];
	}
	
	
}