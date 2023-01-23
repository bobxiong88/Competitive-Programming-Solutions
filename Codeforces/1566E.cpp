#include <bits/stdc++.h>
using namespace std;
#define mx int(2e5)+5
vector<int> g[mx];
int bud;
int dp[mx];
int dfs(int u, int p){
    bool leaf = 0;
    vector<int> t;
    int k = 0;
    for (auto v: g[u]){
        if (v == p) continue;
        dfs(v, u);
        t.push_back(dp[v]);
        k += dp[v];
        if (dp[v] == 0) leaf = true;
    }
    if (t.size() == 0 || k == t.size()){
        dp[u] = 0;
    }
    else{
        dp[u] = 1;
        if (u != 1) bud++;
    }
    return leaf;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int sex;
    cin >>sex;
    while(sex--){
        int n, a, b;
        cin >> n;
        bud = 0;
        for (int i = 0; i<n-1; i++){
            cin >> a >> b;
            g[a].push_back(b);
            g[b].push_back(a);
        }
        int shit = dfs(1,1);
        cout << n-2*bud-shit<< "\n";
        for (int i = 0; i<=n; i++){
            g[i].clear();
        }
    }
}
