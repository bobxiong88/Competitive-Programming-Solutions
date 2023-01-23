#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pog = int;
#define int ll
#define mx int(5e5)+5
#define pb push_back
#define mp make_pair
#define pii pair<pog,int>
#define inf int(1e18)
int d[2][mx], dist[mx];
bitset<mx> sub; // nodes in subtree connecting K points
vector<pii> adj[mx], g[mx];
int monk;
void dfs(int node, int p, int k){
    for (auto[n,w]:g[node]){
        if (n==p) continue;
        d[k][n] = d[k][node]+w;
        dfs(n, node, k);
    }
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, a, b, c, K;
    cin >> N >> K;
    int s = 0;
    for (int i = 1; i<N; i++){
        cin >> a >> b >> c;
        adj[a].pb(mp(b, c));
        adj[b].pb(mp(a, c));
    }

    for (int i = 0; i<K; i++){
        cin >> a;
        if (!i){
            monk = a;
        }
        sub[a] = 1;
    }

    for (int i = 1; i<=N; i++){
        dist[i] = inf;
    }

    queue<int> que;
    que.push(monk);
    dist[monk] = 0;
    while (!que.empty()){
        int node = que.front(); que.pop();
        for (auto [n, w]: adj[node]){
            if (dist[n] > dist[node]+w){
                dist[n] = dist[node]+w;
                que.push(n);
            }
        }
    }

    for (int i = 1; i<=N; i++){
        if (sub[i]) que.push(i);
    }

    while(!que.empty()){
        int node = que.front(); que.pop();
        for (auto[n, w] : adj[node]){
            if (dist[n] < dist[node]){
                s += 2*w;
                g[n].pb(mp(node, w));
                g[node].pb(mp(n, w));
                //cout << n << " " << node << "\n";
                if (!sub[n]){
                    sub[n] = true;
                    que.push(n);
                }
            }
        }
    }

    // thanks thomas: https://dmoj.ca/src/2980425
    dfs(monk, monk, 0);
    a = max_element(d[0]+1, d[0]+N+1)-d[0];
    d[0][a] = 0;
    dfs(a, a, 0);
    b = max_element(d[0]+1, d[0]+N+1)-d[0];
    dfs(b, b, 1);

    queue<pii> que2;

    for (int i = 1; i<=N; i++){
        if (sub[i]) {
            dist[i] = s-max(d[0][i], d[1][i]);
            que2.push(mp(i, dist[i]));
        }
    }

    while (!que2.empty()){
        pii p = que2.front();que2.pop();
        int node = p.first;
        int res = p.second;
        for (auto[n, w]: adj[node]){
            if (!sub[n]){
                sub[n] = true;
                dist[n] = res+w;
                que2.push(mp(n, dist[n]));
            }
        }
    }



    for (int i = 1; i<=N; i++){
        cout << dist[i] << "\n";
    }

}