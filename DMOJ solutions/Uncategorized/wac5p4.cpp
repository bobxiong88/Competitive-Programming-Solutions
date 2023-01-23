#include <bits/stdc++.h>
using namespace std;
#define mx 200005
#define l 18
#define pb push_back
#define pi pair<int,int>
#define mp make_pair
int N, Q, cnt;
vector<int> adj[mx];
int up[mx][l+1];
int par[mx], ht[mx], tin[mx], tout[mx];
void lift(int node, int p, int h){
    cnt++;
    tin[node] = cnt;
    ht[node] = h;
    up[node][0] = p;
    if (h){
        for (int i = 1; i<floor(log2(h))+1; i++)
            up[node][i] = up[up[node][i-1]][i-1];
    }
    for (int n: adj[node]){
        if (n == p) continue;
        lift(n, node, h+1);
    }
    tout[node] = cnt;
}
int ans(int node, int k){
    bitset<l> bit(k);
    int res = node;
    for (int i = 0; i<bit.size(); i++){
        if (bit[i]) res = up[res][i];
    }
    return res;
}
bool check (int a, int b){
    if (tin[a] <= tin[b] && tout[b] <= tout[a])
        return true;
    return false;
}
int lca(int a, int b){
    if (a == b) return a;
    if (check(a, b)) return a;
    if (check(b, a)) return b;
    for (int i = l; i>=0; i--){
        if (!check(up[a][i], b)) a = up[a][i];
    }
    return up[a][0];
}
pi sorted(int a, int b){
    return mp(min(a,b), max(a,b));
}
bool path(int a, int b, int x){
    if (sorted(lca(x,a), lca(x,b)) == sorted(lca(a,b), x))
        return true;
    return false;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int a, b, c, d, dist, ac, x, k, da, dc, res;
    for (int i = 0; i<mx; i++){
        for (int j = 0; j<=l; j++){
            up[i][j] = 1;
        }
        par[i] = i;
    }
    cin >> N >> Q;
    for (int i = 0; i<N-1; i++){
        cin >> a >> b;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    lift(1,1,0);
    while (Q--){
        cin >> a >> b >> c >> d;
        if (a == c){
            cout << 0 << "\n";
            continue;
        }
        ac = lca(a, c);
        dist = ht[a]+ht[c]-2*ht[ac];
        if (dist%2){
            cout << -1 << "\n";
            continue;
        }
        k = dist/2;
        da = ht[a]-ht[ac];
        dc = ht[c]-ht[ac];
        if (da > dc){
            x = ans(a, k);
            res = ht[a]-ht[x];
        }
        else if(da < dc){
            x = ans(c, k);
            res = ht[c]-ht[x];
        }
        else{
            x = ac;
            res = ht[a]-ht[x];
        }
        if (x == b || x == d){
            cout << -1 << "\n";
            continue;
        }
        if (path(a,b,x) && path(c,d,x))
            cout << res << "\n";
        else
            cout << -1 << "\n";
    }
}