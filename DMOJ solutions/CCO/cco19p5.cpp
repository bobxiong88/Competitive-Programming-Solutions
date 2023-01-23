#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define mx int(1e5)+5

set<int> graph[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M, a, b;
    cin >> N >> M;
    for (int i = 0; i<M; i++){
        cin >> a >> b;
        graph[a].insert(b);
    }
    ll ans = 0;
    for (int i = 1; i<=N; i++){
        ans += graph[i].size();
        if (graph[i].size() < 2) continue;
        int k = *graph[i].begin();
        graph[i].erase(graph[i].begin());
        if (graph[i].size() > graph[k].size()) swap(graph[i], graph[k]);
        for (int j: graph[i]) graph[k].insert(j);
    }
    cout << ans << "\n";
}