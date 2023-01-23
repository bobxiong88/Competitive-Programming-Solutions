// this dude carried: https://robert1003.github.io/2020/01/16/centroid-decomposition.html#a-hrefhttpwcipegcomproblemioi1112ioi11---racea
#include <bits/stdc++.h>
using namespace std;
#define mx 100005

int n, m, a, b, t, v, x, res;
set<int> adj[mx];
map<int,int> dist[mx];
int sz[mx], par[mx], ans[mx];
int dfs(int node, int p){
    sz[node] = 1;
    for (auto v: adj[node]){
        if (v == p) continue;
        sz[node] += dfs(v, node);
    }
    return sz[node];
}
void dfs2(int node, int p, int c, int d){
    dist[c][node] = d;
    for (auto v: adj[node]){
        if (v == p) continue;
        dfs2(v, node, c, d+1);
    }
}
int centroid(int node, int p, int s){
    for (auto v: adj[node]){
        if (v == p) continue;
        if (sz[v] > s/2) return centroid(v, node, s);
    }
    return node;
}
void build(int node, int p){
    int s = dfs(node, p);
    int c = centroid(node, p, s);
    if(p == -1) p = c;
    par[c] = p;
    dfs2(c, p, c, 0);
    vector<int> edge(adj[c].begin(), adj[c].end());
    for (auto v: edge){
        adj[c].erase(v);
        adj[v].erase(c);
        build(v, c);
    }
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> n >> m;
    for (int i = 0; i<mx; i++){
        adj[i].clear();
        dist[i].clear();
        ans[i] = 1e9;
    }
    for (int i = 0; i<n-1; i++){
        cin >> a >> b;
        adj[a].insert(b);
        adj[b].insert(a);
    }
    build(1, 0);
    for (int node = 1; node != 0; node = par[node])
        ans[node] = min(ans[node], dist[node][1]);
    while (m--){
        cin >> t >> x;
        if (t == 1){
            for (int node = x; node!=0; node = par[node]) ans[node] = min(ans[node], dist[node][x]);
        }
        else{
            res = 1e9;
            for (int node = x; node != 0; node = par[node]) res = min(res, ans[node] + dist[node][x]);
            if (res == 1e9) res = -1;
            cout << res << "\n";
        }

    }
}
