#include <bits/stdc++.h>
using namespace std;
#define mx 605
#define inf 1000000000
#define pb push_back
const int off = 300;
int dp[mx][mx];
int racism[mx];
vector<int> adj[mx];
void dfs(int node){
    for (auto n: adj[node]) dfs(n);
    int k;
    if (racism[node]){
        k=1;
    }
    else{
        k=-1;
    }
    if (adj[node].size() == 0){
        dp[node][k+off] = 0;
    }
    else if (adj[node].size()==1){
        int n = adj[node][0];
        for (int i = -300; i<=300; i++){
            if (dp[n][i+off]==inf) continue;
            dp[node][k+i+off] = dp[n][i+off];
        }
        // castration
        dp[node][k+off] = min(1, dp[node][k+off]);
    }
    else{
        int u = adj[node][0];
        int v = adj[node][1];
        // cut none
        for (int i = -300; i<=300; i++){
            if (dp[u][i+off]==inf) continue;
            for (int j = -300; j<=300;j++){
                if (dp[v][j+off]==inf) continue;
                dp[node][k+i+j+off] = min(dp[node][k+i+j+off], dp[u][i+off]+dp[v][j+off]);
                //cout << node << " " << k+i+j << " " << dp[node][k+i+j+off] << "\n";
            }
        }
        // cut left
        for (int i = -300; i<=300; i++){
            if (dp[u][i+off]==inf) continue;
            dp[node][k+i+off] = min(dp[u][i+off]+1, dp[node][k+i+off]);
        }
        // cut right
        for (int j = -300; j<=300; j++){
            if (dp[v][j+off]==inf) continue;
            dp[node][k+j+off] = min(dp[v][j+off]+1, dp[node][k+j+off]);
        }
        // cut both
        dp[node][k+off] = min(2, dp[node][k+off]);
    }

}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, D, C, c, x, y;
    cin >> N >> D;
    for (int i = 0; i<N; i++){
        cin >> x >> c >> C;
        racism[x] = c;
        while(C--){
            cin >> y;
            adj[x].pb(y);
        }
    }
    for (int i = 0; i<mx; i++){
        for (int j = 0; j<mx;j++){
            dp[i][j]=inf;
        }
    }
    dfs(0);
    if (dp[0][D+off] == inf) dp[0][D+off] = -1;
    cout << dp[0][D+off] << "\n";
}