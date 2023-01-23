#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define m 1000000007
#define mx 100005
vector<int> order;
vector<vector<int>> adj(mx);
vector<int> inzero;
vector<map<int,int>> dp(mx);
bool vis[mx] = {false};
void top(int node){
    vis[node] = true;
    for(int n: adj[node]){
        if (!vis[n]) top(n);
    }
    order.push_back(node);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int N, M, a, b;
    cin >> N >> M;
    while(M--){
        cin >> a >> b;
        adj[a].push_back(b);
    }
    for(int i = 1; i<=N; i++){
        if(!vis[i]){
            inzero.push_back(i);
            top(i);
        }
    }
    reverse(order.begin(), order.end());
    for(int i: inzero){
        dp[i].insert(pair<int,int>(0,1));
    }

    for(int node: order){
        for(int n: adj[node]){
            for(map<int, int>::iterator it = dp[node].begin(); it != dp[node].end(); it++){
                int k = it->first+1;
                int v = it->second;
                if(dp[n].find(k) == dp[n].end()){
                    dp[n].insert(pair<int,int>(k, v));
                }
                else{
                    dp[n][k] += v;
                    dp[n][k] %= m;
                }
            }
        }
    }
    ll ans = 0;
    for(int n = 1; n<=N; n++){
        if (adj[n].size()) continue;
        for(map<int, int>::iterator it = dp[n].begin(); it != dp[n].end(); ++it){
            ll i = it->first;
            ll v = it->second;
            ans += i*v;
            ans %= m;
        }
    }
    cout << ans;
}