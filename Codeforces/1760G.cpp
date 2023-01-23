#include <bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define mx int(2e5)
vector<pii> g[mx];
vector<int> fa;
vector<int> fb;
void dfs1(int u, int p, int x, int b){
    for (auto [v,w]: g[u]){
        if (v == p) continue;
        if (v == b) continue;
        dfs1(v, u, w^x, b);
        fa.pb(w^x);
    }
}
void dfs2(int u, int p, int x){
    for (auto [v,w]: g[u]){
        if (v == p) continue;
        dfs2(v, u, w^x);
        fb.pb(w^x);
    }
}
int main(){
    int t;
    cin >> t;
    while (t--){

        fa.clear();
        fb.clear();
        int u, v, w, n, a, b;
        cin >> n >> a >> b;
        for (int i = 0; i<=n; i++) g[i].clear();
        for (int i = 0; i<n-1; i++){
            cin >> u >> v >> w;
            g[u].pb(mp(v,w));
            g[v].pb(mp(u,w));
        }
        fa.pb(0);
        dfs1(a,a,0,b);
        dfs2(b,b,0);
        set<int> s;
        for (auto k: fb){
            s.insert(k);
        }
        string ans = "NO";
        for (auto i: fa){
            if (s.count(i)) ans = "YES";
        }
        cout << ans << "\n";
    }
}
