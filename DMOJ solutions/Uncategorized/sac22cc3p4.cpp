#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
const int mx = 2e5+5;
const int bit = 19;
int cnt, in[mx], out[mx], up[mx][bit], ht[mx], sz[mx], par[mx];
vector<int> adj[mx];
void dfs(int node, int p){
    ht[node] = ht[p] + 1;
    in[node] = ++cnt; up[node][0] = p;
    for (int i = 1; i<bit; i++) up[node][i] = up[up[node][i-1]][i-1];
    for (auto n: adj[node]){
        if (n == p) continue;
        dfs(n, node);
    }
    out[node] = cnt;
}
bool check(int a, int b){
    return in[a] <= in[b] && out[a] >= out[b];
}
int lca(int a, int b){
    if (check(a,b)) return a;
    if (check(b,a)) return b;
    for (int i = bit-1; i>=0; i--){
        if (!check(up[a][i], b)) a = up[a][i];
    }
    return up[a][0];
}
int dist(int a, int b){
    int c = lca(a,b);
    return ht[a]+ht[b]-2*ht[c];
}
int find_set(int v){
    if (v == par[v]) return v;
    return par[v] = find_set(par[v]);
}
void join(int a, int b){
    a = find_set(a); b = find_set(b);
    if (a == b) return;
    par[b] = a;
    sz[a] += sz[b];
}
struct q{
    int t, u, v;
};
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, t, u, v, s;
    cin >> N >> Q;
    for (int i = 1; i<=N; i++){
        par[i] = i;
        sz[i] = 1;
    }
    for (int i = 0; i<N-1; i++){
        cin >> s >> t;
        adj[s].pb(t);
        adj[t].pb(s);
    }
    dfs(1,1);
    vector<q> queries;
    for (int i = 0; i<Q; i++){
        cin >> t >> u >> v;
        queries.pb({t,u,v});
    }
    reverse(queries.begin(), queries.end());
    vector<int> res;
    for (auto [t, u, v]: queries){
        if (t == 1){
            if (find_set(u)==find_set(v)) res.pb(dist(u,v));
            else res.pb(-1);
        }
        else{
            join(u,v);
        }
    }
    reverse(res.begin(), res.end());
    for (auto k: res){
        cout << k << "\n";
    }
}