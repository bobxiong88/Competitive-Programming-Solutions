#include <bits/stdc++.h>
using namespace std;
vector <pair<int,int>> adj[500001];
int MAXN = 1000000005;
int dist[500001];
int roots[500001][2];
int node;
int main(){
    int N, u, v, w;
    cin >> N;
	for(int i = 0; i<500001; i++)
		dist[i] = MAXN;
    for(int i = 0; i<N-1; i++){
        cin >> u >> v >> w;
        adj[u].push_back(make_pair(v,w));
        adj[v].push_back(make_pair(u,w));
    }
    vector<int>nodes;
    queue<int> que;
    int far = 1;
    int d = 0;
    dist[1] = 0;
    que.push(1);
    nodes.push_back(1);
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
    //cout << far << "|" << d << "\n";
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
    cout << d << "\n";
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
    cout << radius;
}