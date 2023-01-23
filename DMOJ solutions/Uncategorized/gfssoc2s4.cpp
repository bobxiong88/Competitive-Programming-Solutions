#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
using ll = long long;
#define int ll
int inf = 999999999999999;
vector<int> bfs(int start, vector<vector<pair<int,int>>> graph){
    vector <int> dist(graph.size());
    for(int i = 0; i<graph.size(); i++){
        dist[i] = inf;
    }
    dist[start] = 0;
    queue<pair<int,int>> que;
    que.push(make_pair(start, 0));
    while (!que.empty()){
        int node = que.front().first;
        int d = que.front().second;
        que.pop();
        if(dist[node] < d) continue;
        for (auto edge : graph[node]){
            int n = edge.first;
            int w = edge.second;
            if(dist[n]>d+w){
                dist[n] = d+w;
                que.push(make_pair(n, d+w));
            }
        }
    }
    return dist;
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n, m, a, b, k, g, d;
    cin >> n >> m;
    vector<vector<pair<int,int>>> g1(n+1);
    vector<vector<pair<int,int>>> g2(n+1);
    for(int i = 0; i<m; i++){
        cin >> a >> b >> k;
        g1[a].push_back(make_pair(b,k));
        g2[b].push_back(make_pair(a,k));
    }
    cin >> d;
    vector<int> start = bfs(1, g1);
    vector<int> endd = bfs(n, g2);
    int ans = start[n];
    for(int i = 0; i<d; i++){
        cin >> a >> b >> g;
        ans = min(ans, start[a]+g+endd[b]);
    }
    if (ans >= inf) ans = -1;
    cout << ans;
}