#include <bits/stdc++.h>
#include <queue>
#include <vector>

using namespace std;
int Avisited[100001];
int Bvisited[100001];
int disjoint[100001];
//int epic[100001];
/*
5 3 3
1 4
4 2
3 5
1 3
1 2
3 4
*/
int find_set(int v){
	if (v == disjoint[v]){
		return v;
	}
	return disjoint[v] = find_set(disjoint[v]);
}
void union_sets(int rank[], int a, int b){
	a = find_set(a);
	b = find_set(b);
	if (a!=b){
		if(rank[a]<rank[b]){
			swap(a,b);
		}
		disjoint[b] = a;
		if(rank[a]==rank[b]){
			rank[a]++;
		}
		
	}
}

int main(){
	std::ios_base::sync_with_stdio(false);
	int rank[100001];
	memset(rank,0,sizeof(rank));
	for(int i = 0;i<100001;i++){
		disjoint[i] = i;
	}

	int N,M,Q;
	
	cin >> N >> M >>Q;
	vector<list<int>> adj(N+1);
	
	
	
	int a,b;
	for(int i = 0; i<M; i++){
		cin>>a>>b;
		adj[a].push_back(b);
		adj[b].push_back(a);
		
		union_sets(rank,a,b);
	}


	int answer, node, type, temp, gamer;
	int big = -1;

	for(int q = 0; q<Q; q++){
		cin >>a>>b;
		answer = -1;
		if (a==b){
			answer = 0;
		}
		else if(find_set(a)!=find_set(b)){
			
		}else{
				queue<pair<int,int>> que;

		que.push(make_pair(a,0));
		que.push(make_pair(b,1));
		
		memset(Avisited, big, sizeof(Avisited));
		memset(Bvisited, big, sizeof(Bvisited));
		
		
		Avisited[a] = 0;
		Bvisited[b] = 0;	    
		
		while(!que.empty()){
		

			node = que.front().first;
			type = que.front().second;
			que.pop();
			for(int n:adj[node]){
				if(type == 0){
					if(Avisited[n]==big){
						
						if (Bvisited[n] != big){
							answer = Bvisited[n]+Avisited[node]+1;
							break;
								
						}
						Avisited[n] = Avisited[node]+1;
						que.push(make_pair(n,0));
					}
				}
				else{
					if(Bvisited[n]==big){
						

						if (Avisited[n] != big){
							answer = Avisited[n]+Bvisited[node]+1;
							break;
								
						}
						Bvisited[n] = Bvisited[node]+1;
						que.push(make_pair(n,1));
					}
				}

			}
			if(answer!=-1){
				break;
			}
		}
		
		
	}
	//int gamer = max(answer,gamer);
	//cout<<answer<<"\n";
	printf("%d\n",answer);
}

//cout<<gamer<<endl;
    
}