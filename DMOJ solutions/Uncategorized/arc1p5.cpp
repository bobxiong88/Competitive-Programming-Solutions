#include <bits/stdc++.h>
using namespace std;
#define pb push_back
int pars[10005][5005];
int ans[300005];
int find_par(int i, int u){
    if (pars[i][u] == u) return u;
    return pars[i][u] = find_par(i,pars[i][u]);
}
void join(int i, int u, int v){
    u = find_par(i,u);
    v = find_par(i, v);
    if (u == v) return;
    pars[i][v] = u;
}
struct quartet{
    int u, v, w, i;
};
bool comp(const quartet &a, const quartet &b){
    return a.w < b.w;
}
int main(){
    int N, M, K,u , v, w;
    cin >> N >> M >> K;
    for (int i = 0; i<=K; i++){
        for (int j = 1; j<=N; j++){
            pars[i][j] = j;
        }
    }
    for (int i = 0; i<M; i++) ans[i] = -1;
    vector<quartet> edges;
    for (int i = 0; i<M; i++){
        cin >> u >> v >> w;
        edges.pb({u, v, w, i});
    }
    sort(edges.begin(), edges.end(), comp);
    for (auto [u,v,w,i]: edges){
        int l = 1;
        int r = K;
        int res = 1000000000;
        while (l <= r){
            int m = (l+r)/2;
            if (find_par(m,u)!=find_par(m,v)){
                r = m-1;
                res = m;
            }
            else{
                l = m+1;
            }
        }
        if (res != 1000000000){
            ans[i] = res;
            join(res,u,v);
        }
    }
    for (int i = 0; i<M; i++) cout << ans[i] << "\n";
}