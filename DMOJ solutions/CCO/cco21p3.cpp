#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll

#define smol 800005
#define mx 1600005
#define pii pair<int,int>
#define mp make_pair
#define pb push_back

int N, Q, cnt;
int c[mx], idx[mx], ans[mx], posp[mx], par[mx], bit[mx], curr[mx];
vector<pii> store[mx];
vector<vector<int>> tour;
vector<vector<int>> g;

int lsb(int x){return x&(-x);}
int qry(int x){
    int res = 0;
    for (int i = x; i>0; i-=lsb(i)) res += bit[i];
    return res;
}
void amogus(int x, int v){
    for (int i = x; i<mx; i+=lsb(i)) bit[i] += v;
}
int bs(int l, int r, int pos){
    while (l<=r){
        int m = (l+r)/2;
        int a = qry(m-1);
        int b = qry(m);
        if (a < pos && pos == b) return m;
        if (b < pos) l = m+1;
        else r = m-1;
    }
}
void dfs(int u, int p){
    if (u != 1) tour[u][0] = tour[p][idx[u]];
    for (int i = 1; i<c[u]; i++){
        tour[u][i] = tour[u][i-1];
        //int v = g[u][i];
    }
    bool seen = false;
    for (int i = 0; i<c[u]; i++){
        if (seen) tour[u][i]++;
        if (g[u][i] == p) seen = true;
    }
    for (int v: g[u]){
        if (v!=p) dfs(v, u);
    }
}
void euler(int u, int p){
    store[u].pb(mp(cnt, p));
    cnt++;
    int x;
    if (u == 1) x = 0;
    else{
        for (int i = 0; i<c[u]; i++){
            if (g[u][i] == p){
                x = i+1;
                break;
            }
        }
    }
    for (int i = 0; i<c[u]; i++){
        int v = g[u][(x+i)%c[u]];
        if (v == p) continue;
        euler(v, u);
        store[u].pb(mp(cnt, v));
        cnt++;
    }
}
void get(int u, int p){
    par[u] = p;
    for (int i = 0; i<c[u]; i++){
        int v = g[u][i];
        if (v != p){
            idx[v] = i;
            get(v, u);
        }
        else{
            posp[u] = i+1;
        }
    }
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> Q;
    vector<int> emp;
    vector<pii> app(mx, mp(0,0));
    g.pb(emp);
    tour.pb(emp);
    for (int i = 1; i<N+1; i++){
        cin >> c[i];
        vector<int> adj(c[i]);
        cin >> adj[c[i]-1];
        for (int j = 0; j<c[i]-1; j++) cin >> adj[j];
        g.pb(adj);
        vector<int> t(c[i], 1);
        tour.pb(t);
    }
    vector<pii> query;
    for (int i = 0; i<Q; i++){
        int x;
        cin >> x;
        query.pb(mp(x, i));
    }
    sort(query.begin(), query.end());
    reverse(query.begin(), query.end());
    cnt = 0;
    get(1, 1);
    dfs(1, 1);
    euler(1, 1);
    int tot = 0;
    for (int u = 1; u<N+1; u++){
        int st = posp[u];
        for (int i = 0; i<c[u]; i++){
            int x = (i-st+c[u]*2)%c[u];
            auto [a, b] = store[u][x];
            app[a] = mp(u, tour[u][i]);
            tot = max(tot, tour[u][i]);
        }
    }
    int k = 0;
    int killme = 0;
    vector<pii> meme[tot+1];
    for (int i = 0; i<2*N-2; i++){
        auto [a, b] = app[i];
        meme[b].pb(mp(a, i+1));
    }
    for (int i = 1; i<tot+1; i++){
        for (auto [a, j]: meme[i]){
            curr[j] = a;
            amogus(j, 1);
            killme++;
        }
        int p = k;
        k += killme-1;
        while (!query.empty() && query.back().first <= k){
            auto [x, i] = query.back(); query.pop_back();
            int pos = x-p+1;
            int res = bs(1, 2*N-1, pos);
            ans[i] = curr[res];
        }
        k++;
    }
    int q = int(1e17)/(2*N-2);
    for (auto [x, i]: query){
        int a = x-k;
        int m = 2*N-2;
        a += q*m;
        ans[i] = curr[a%m+1];
    }
    for (int i = 0; i<Q; i++) cout << ans[i] << "\n";
}