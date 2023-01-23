#include <bits/stdc++.h>
using namespace std;
#define M 1000000
vector<vector<int>> adj(M);
int P[M];
int ht[M] = {0};
int dfs(int node, int p, int h){
    ht[node] = h;
    for (auto n: adj[node]){
        if (n == p) continue;
        P[node] += dfs(n, node, h+1);
    }
    return P[node];
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int s = 0;
    int N, a, b;
    cin >> N;
    for (int i = 0; i<N; i++){
        cin >> P[i];
        s += P[i];
    }
    for (int i = 0; i<N-1; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    dfs(0, -1, 0);
    int mx = 2100000000;
    int ans = 0;
    for (int node = 0; node < N; node++){
        int curr = 0;
        for (auto n: adj[node]){
            if (ht[n] < ht[node]) curr = max(curr, s-P[node]);
            else curr = max(curr, P[n]);
        }
        if (curr < mx){
            mx = curr;
            ans = node;
        }
    }
    cout << ans;
    return 0;
}