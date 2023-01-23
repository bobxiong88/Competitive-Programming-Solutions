#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx 705
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
int h[mx][mx], v[mx][mx], par[mx*mx], sz[mx*mx];
int leader(int a){
    if (a == par[a]) return a;
    return leader(par[a]);
}

int gcd(int a, int b){
    if (!a) return b;
    return gcd(b%a, a);
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, x, y, a, b, g;
    int d[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    vector<pii> rem;
    map<pii, vector<pii>> edges;
    cin >> N;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> h[i][j];
            par[i*N+j] = i*N+j;
            sz[i*N+j] = 1;
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> v[i][j];
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            for (int k = 0; k < 4; k++){
                x = d[k][0]+i;
                y = d[k][1]+j;
                if (x >= N || x < 0 || y >= N || y < 0) continue;
                if (v[x][y] == v[i][j]){
                    if (h[x][y] == h[i][j]) rem.pb(mp(x*N+y,i*N+j));
                    continue;
                }
                float t = (h[x][y]-h[i][j])/(v[i][j]-v[x][y]);
                if (t < 0) continue;
                a = (h[x][y]-h[i][j])*v[i][j]+(v[i][j]-v[x][y])*h[i][j];
                b = v[i][j]-v[x][y];
                if (a/b < 0) continue;
                a = abs(a); b = abs(b);
                g = gcd(a,b);
                a /= g; b /= g;
                edges[mp(a,b)].pb(mp(i*N+j, x*N+y));
            }
        }
    }
    for (auto [a, b] : rem){
        a = leader(a); b = leader(b);
        if (a == b) continue;
        if (sz[a] < sz[b]) swap(a, b);
        par[b] = a;
        sz[a] += sz[b];
    }
    int ans = 0;
    for (auto [key, value] : edges){
        vector<pii> used;
        int res = 0;
        for (auto [a, b] : value){
            a = leader(a); b = leader(b);
            if (a == b) continue;
            if (sz[a] < sz[b]) swap(a,b);
            par[b] = a;
            sz[a] += sz[b];
            used.pb(mp(a,b));
            res = max(res, sz[a]);
        }
        ans = max(res, ans);
        reverse(used.begin(), used.end());
        for (auto[a, b]:used){
            par[a] = a;
            par[b] = b;
            sz[a] -= sz[b];
        }
    }
    cout << ans;
}