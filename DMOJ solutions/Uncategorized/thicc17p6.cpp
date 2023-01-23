#include <bits/stdc++.h>
using namespace std;
#define mx int(2e5)+5
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
int down[mx], up[mx];
multiset<int> lt[mx];
vector<pii> g[mx];
void dfs(int node, int p){
    for (auto[n,w]:g[node]){
        if (n==p) continue;
        dfs(n, node);
        down[node] = max(down[node], down[n]+w);
        lt[node].insert(down[n]+w);
    }
}
void dfs2(int node, int p, int w){
    if (node!=1){
        lt[p].erase(down[node]+w);
        up[node] = max(up[p]+w, *max_element(lt[p].begin(), lt[p].end())+w);
        lt[p].insert(down[node]+w);
    }
    for (auto[n, w]:g[node]){
        if(n==p) continue;
        dfs2(n, node, w);
    }

}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, T, a, b, c;
    cin >> N >> T;
    int s = 0;
    for (int i = 1; i<N; i++){
        cin >> a >> b >> c;
        g[a].pb(mp(b, c));
        g[b].pb(mp(a, c));
        s += 2*c;
    }
    dfs(1, 1);
    dfs2(1, 1, 0);
    for (int i = 1; i<=N; i++){
        //cout << down[i] << " " << up[i] << "\n";
    }
    for (int i = 1; i<=N; i++){
        if (g[i].size() == T) cout << i << " " << s-max(down[i], up[i]) << "\n";
    }
}