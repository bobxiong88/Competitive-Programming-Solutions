#include <bits/stdc++.h>
using namespace std;
vector <pair<int,int>> adj[100005];
int MAXN = 1000000005;
int dist[100005];
int roots[100005][2];
int node;
vector<int>radi;
int diam = -1;
void travelTime(int N, int M, int L, int A[], int B[], int T[]){
	for(int i = 0; i<100000; i++)
		dist[i] = MAXN;
	for(int i = 0; i < M; i++){
		adj[A[i]].push_back(make_pair(B[i], T[i]));
		adj[B[i]].push_back(make_pair(A[i], T[i]));
	}
	for(int i = 0; i < N; i++){
		if(dist[i]==MAXN){
			vector<int>nodes;
			queue<int> que;
			int far = i;
			int d = 0;
			dist[i] = 0;
			que.push(i);
			nodes.push_back(i);
			while(!que.empty()){
				node = que.front(); que.pop();
				if(dist[node]>d)
                {
					far = node;
					d = dist[node];
                }

				for(auto [n,w]: adj[node]){
					if(w+dist[node]<dist[n]){
						dist[n] = w + dist[node];
						que.push(n);
						nodes.push_back(n);
					}
				}
			}
			for(auto&n: nodes)
				dist[n] = MAXN;

			int start = far;
			nodes.clear();
			que.push(far);
			dist[far] = 0;
			d = 0;
			nodes.push_back(far);
			while(!que.empty()){
				node = que.front(); que.pop();
				if(dist[node]>d){
					far = node;
					d = dist[node];
				}
				for(auto [n,w]: adj[node]){
					if(w+dist[node]<dist[n]){
						dist[n] = w + dist[node];
						que.push(n);
						nodes.push_back(n);
						roots[n][0] = node;
						roots[n][1] = w;
					}
				}
			}
			diam = max(diam, d);
			vector<int>edges;
			que.push(far);
			while(true){
				node = que.front(); que.pop();
				if(node==start)
					break;
				que.push(roots[node][0]);
				edges.push_back(roots[node][1]);
			}
			int left = accumulate(edges.begin(), edges.end(), 0), right = 0;
			int diff = MAXN;
			int radius = 0;
			for(auto edge: edges){
				left -= edge;
				right += edge;
				if(abs(left-right)<diff){
					radius = max(left,right);
					diff = abs(left-right);
				}
				if(abs(left-right)==diff)
					radius = max(radius, max(left, right));
			}
			radi.push_back(radius);
		}
	}
	sort(radi.begin(), radi.end(), greater<int>());
	int time = diam;
	if(radi.size()>1)
        time = max(time, radi[0] + radi[1]+L);
	if(radi.size()>2)
        time = max(time, radi[1] + radi[2] + (2*L));
	cout << time;
}
int N, M, L;
int A[100005];
int B[100005];
int T[100005];
int main(){
    cin >> N >> M >> L;
    for (int i = 0; i<M; i++){
        cin >> A[i] >> B[i] >> T[i];
    }
	travelTime(N, M, L, A, B, T);
}