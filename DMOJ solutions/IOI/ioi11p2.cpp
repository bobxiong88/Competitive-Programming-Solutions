// this dude carried: https://robert1003.github.io/2020/01/16/centroid-decomposition.html#a-hrefhttpwcipegcomproblemioi1112ioi11---racea
#include <bits/stdc++.h>
using namespace std;
#define mx 200005
#define pi pair<int,int>
#define mp make_pair
int n, a, b, w, res, ans, k;
set<pi> adj[mx];
map<int,int> dist;
vector<pi> balls;
int sz[mx];
int dfs(int node, int p){
    sz[node] = 1;
    for (auto v: adj[node]){
        if (v.first == p) continue;
        sz[node] += dfs(v.first, node);
    }
    return sz[node];
}
void dfs2(int node, int p, int d, int cost){
    int get = k-cost;
    if (get >=0 && dist.count(get)){
        ans = min(ans, d + dist[get]);
    }
    if (cost <= k){
        balls.push_back(mp(d, cost));
        for (auto v: adj[node]){
            if (v.first == p) continue;
            dfs2(v.first, node, d+1, cost + v.second);
        }
    }
}
int centroid(int node, int p, int s){
    for (auto v: adj[node]){
        if (v.first == p) continue;
        if (sz[v.first] > s/2) return centroid(v.first, node, s);
    }
    return node;
}
void build(int node, int p){
    int s = dfs(node, p);
    int c = centroid(node, p, s);
    dist.clear();
    dist[0] = 0;
    vector<pi> edge(adj[c].begin(), adj[c].end());
    for (auto v: edge){
        balls.clear();
        dfs2(v.first, c, 1, v.second);
        for (auto ball: balls){
            if (dist.count(ball.second)) dist[ball.second] = min(dist[ball.second], ball.first);
            else dist[ball.second] = ball.first;
        }
    }
    for (auto v: edge){
        adj[c].erase(v);
        adj[v.first].erase(mp(c, v.second));
        build(v.first, c);
    }
}
int best_path(int N, int K, int H[][2], int L[]){
    n = N; k = K;
    for (int i = 0; i<n-1; i++){
        a = H[i][0]; b = H[i][1]; w = L[i];
        adj[a].insert(mp(b,w));
        adj[b].insert(mp(a,w));
    }
    ans = 1e9;
    build(0, -1);
    if (ans == 1e9) ans = -1;
    return ans;
}
int main(){

}