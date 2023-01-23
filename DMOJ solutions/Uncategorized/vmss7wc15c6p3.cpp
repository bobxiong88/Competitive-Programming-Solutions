#include <bits/stdc++.h>
using namespace std;
#define mx 400005
#define pb push_back
int dp[mx];
int ans, N, a, b;
vector<int> adj[mx];
void dfs(int node, int p){
    for (auto n: adj[node]){
        if (n == p) continue;
        dfs(n, node);
        dp[node] += dp[n];
    }
    ans = max(ans, dp[node]);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    dp[0] = -1e9;
    cin >> N;
    for (int i = 0; i<N-1; i++){
        cin >> a >> b;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    for (int i = 1; i<=N; i++) cin >> dp[i];
    ans = -1e9;
    dfs(1, 1);
    cout << ans;
}