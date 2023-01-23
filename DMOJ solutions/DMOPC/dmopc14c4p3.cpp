#include <iostream>
#include <queue>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main(){
	//vector< pair <int,int> > ;
	queue<pair<int,int>> q;
	
	int L,D;
	cin>>L>>D;
	int grid[D][L];
	int distance[D][L];
	for(int i=0;i<D;i++){
		
		for(int j=0;j<L;j++){
			int a;
			cin>>a;
			grid[i][j] = a;
			distance[i][j] = 200000000;
		}
		
	}
	int tx,ty;
	cin>>tx>>ty;
	
	
	distance[0][0] = grid[0][0];
	
	q.push(make_pair(0,0));
	
	while (!q.empty()){
		int y,x,b,a;
		y=get<0>(q.front());
		x = get<1>(q.front());

		q.pop();
		b = y;
		a = x-1;
		
		
		if(b<D && b>=0 && a>=0 && a<L){
			if(distance[b][a]>distance[y][x]+grid[b][a]){
				q.push(make_pair(b,a));
				distance[b][a] = distance[y][x]+grid[b][a];
			}
		}
		b = y;
		a = x+1;
		
		
		if(b<D && b>=0 && a>=0 && a<L){
			if(distance[b][a]>distance[y][x]+grid[b][a]){
				q.push(make_pair(b,a));
				distance[b][a] = distance[y][x]+grid[b][a];
			}
		}
		b = y+1;
		a = x;
		
		
		if(b<D && b>=0 && a>=0 && a<L){
			if(distance[b][a]>distance[y][x]+grid[b][a]){
				q.push(make_pair(b,a));
				distance[b][a] = distance[y][x]+grid[b][a];
			}
		}
	}
	cout<<distance[ty][tx];
}