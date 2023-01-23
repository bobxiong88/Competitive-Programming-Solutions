#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> pi;
int n, a, b, c, m, ans;
vector<vector<pi>> adj(100005);
void dfs(int node, int p, int d){
    m = max(m, d);
    for(pi &pr : adj[node]){
        if (pr.first == p) continue;
        dfs(pr.first, node, pr.second+d);
    }
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    m = 0;
    ans = 0;
    cin >> n;
    for(int i = 0;i<n;i++){
        cin >> a >> b >> c;
        adj[a].push_back(make_pair(b,c));
        adj[b].push_back(make_pair(a,c));
        ans += c;
    }
    dfs(0,-1,0);
    cout << ans*2-m << "\n";
    return 0;
}