#include <bits/stdc++.h>
using namespace std;
using lol = long long;
//#define int lol
#define mx 100005
#define bit 25
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define inf lol(2e9)
int cnt, in[mx], out[mx], up[mx][bit], ht[mx], c[mx], walk[mx], freq[mx], ans[mx];
const int k = 800;
vector<int> adj[mx];
multiset<int> boob;
multiset<lol> diff;
struct qry{
    int l, r, i, p;
};
vector<qry> queries[mx];
vector<qry> tot;
void dfs(int node, int p){
    ht[node] = ht[p]+1;
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
    if (check(a, b)) return a;
    if (check(b, a)) return b;
    for (int i = bit-1; i >=0; i--){
        if (!check(up[a][i], b))
            a = up[a][i];
    }
    return up[a][0];
}
void dfs2(int u, int p){
    in[u] = cnt;
    walk[cnt] = u;
    cnt++;
    for (int v: adj[u]){
        if (v != p) dfs2(v, u);
    }
    out[u] = cnt;
    walk[cnt] = u;
    cnt++;
}
bool comp(const qry &x, const qry &y){
    return x.r < y.r;
}
void push(int v){
    boob.insert(v);
    lol l = *prev(boob.find(v));
    lol r = *next(boob.find(v));
    lol a = v-l;
    lol b = r-v;
    diff.insert(a); diff.insert(b); diff.erase(diff.find(r-l));
}
void pop(int v){
    lol l = *prev(boob.find(v));
    lol r = *next(boob.find(v));
    lol a = v-l;
    lol b = r-v;
    diff.erase(diff.find(a)); diff.erase(diff.find(b)); diff.insert(r-l);
    boob.erase(boob.find(v));
}
void add(int n){
    freq[n]++;
    if (freq[n]%2) push(c[n]);
    else pop(c[n]);
}
void rem(int n){
    freq[n]--;
    if (freq[n]%2) push(c[n]);
    else pop(c[n]);
}
int get(int x){
    return x/k;
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q;
    cin >> N >> Q;
    for (int i = 1; i<=N; i++) cin >> c[i];
    for (int i = 0; i<N-1; i++){
        int a, b;
        cin >> a >> b;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    dfs(1, 1);
    cnt = 0;
    dfs2(1, 1);

    for (int i = 0; i<Q; i++){
        int u, v;
        cin >> u >> v;
        int p = lca(u, v);
        if (p==u) queries[get(in[u])].pb({in[u], in[v], i, 0});
        if (p==v) queries[get(in[v])].pb({in[v], in[u], i, 0});
        if (in[u] > in[v]) swap(u, v);
        queries[get(out[u])].pb({out[u], in[v], i, p});
    }
    int ll = 0;
    int lr = -1;
    cnt  = 0;
    for (auto blk: queries){
        if (blk.size()==0) continue;
        sort(blk.begin(), blk.end(), comp);

        if (++cnt%2){
            reverse(blk.begin(), blk.end());
        }
        for (auto q : blk) tot.pb(q);
    }
    boob.insert(inf); boob.insert(-inf); diff.insert(2*inf);
    for (auto [l, r, i, p] : tot){
        while (ll > l){
            ll--;
            add(walk[ll]);
        }
        while (lr < r){
            lr++;
            add(walk[lr]);
        }
        while (ll < l){
            rem(walk[ll]);
            ll++;
        }
        while (lr > r){
            rem(walk[lr]);
            lr--;
        }
        if (p) add(p);
        ans[i] = *diff.begin();
        /*cout << l << " " << r <<" " << i << " " << p << " ans is " << ans[i] << "\n";
        cout << "curr "; for (auto e: boob) cout << e << " "; cout << "\n";
        cout << "diff "; for (auto e: diff) cout << e << " "; cout << "\n";
        cout << "\n";
        */
        if (p) rem(p);
    }
    for (int i = 0; i<Q; i++){
        cout << ans[i] << "\n";
    }
}
/*
10 6
1 2 3 4 5 6 7 8 9 10
1 2
1 3
1 4
2 5
2 6
3 7
4 8
8 9
8 10

1 5
5 10
8 9
2 4
3 7
5 6
*/