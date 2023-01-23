#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
//#pragma GCC target("avx,avx2,fma")
using namespace std;
using ll = long long;
#define int ll
#define mx 1000005
struct edge{
    int a, b, w;
};
vector<int> sz(mx,1);
vector<edge> edges;
vector<vector<int>> adj(mx);
int dfs(int node, int p){
    if(!adj[node].size()) return 1;
    for(auto v: adj[node]){
        if (v == p) continue;
        sz[node] += dfs(v, node);
    }
    return sz[node];
}
int a, b, w, n;
main(){
    ios_base::sync_with_stdio(false);  cin.tie(0); cout.tie(0);
    //for (int i = 0; i<mx; i++) sz[i] = 1;
    cin >> n;
    for (int i = 0; i<n-1; i++){
        cin >> a >> b >> w;
        adj[a].push_back(b);
        adj[b].push_back(a);
        edges.push_back({a,b,w});
    }
    dfs(1, -1);
    int ans = 0;
    for(auto e:edges){
        a = e.a;
        b = e.b;
        w = e.w;
        if (sz[a] < sz[b]) swap(a,b);
        ans += abs(n-2*sz[b])*w;
    }
    cout << ans;
}