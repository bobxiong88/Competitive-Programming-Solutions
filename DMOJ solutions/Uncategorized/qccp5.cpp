#include <bits/stdc++.h>
using namespace std;
#define mx int(1e5)+5
#define pii pair<int,double>
#define pb push_back
#define mp make_pair
struct pnt{
    double x, y, z;
};
int N, M, R, T, K, v, a, b;
double x, y, z, d;
vector<pii> g[mx];
int val[mx];
vector<pnt> pos(mx, {0,0,0});
double get(pnt a, pnt b){
    double delta, phi, gc;
    delta = sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2)+pow(a.z-b.z,2));
    phi = asin(double(delta/(2*double(R))));
    gc = 2*phi*double(R);
    return gc;
}
vector<double> bfs(vector<int> &start){
    queue<pii> que;
    vector<double> dist(mx, 1e9);
    for (int i: start){
        dist[i] = 0;
        que.push(mp(i, 0));
    }
    while (!que.empty()){
        pii p = que.front(); que.pop();
        int node = p.first; int d = p.second;
        if (dist[node] < d) continue;
        for (auto[n,w]: g[node]){
            if (dist[node]+w < dist[n]){
                dist[n] = dist[node]+w;
                que.push(mp(n, dist[n]));
            }
        }
    }
    return dist;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> M >> R >> T >> K;
    vector<int> air;
    for (int i = 0; i<K; i++){
        cin >> v;
        air.pb(v);
    }
    for (int i = 1; i<=N; i++){
        cin >> v >> x >> y >> z;
        val[i] = v;
        pos[i] = {x, y, z};
    }
    for (int i = 0; i<M; i++){
        cin >> a >> b;
        d = get(pos[a], pos[b]);
        g[a].pb(mp(b, d));
        g[b].pb(mp(a, d));
    }
    vector<int> temp;
    temp.pb(1);
    vector<double> dist1 = bfs(temp);
    vector<double> dist2 = bfs(air);
    int ans = -1;
    for (int i = 1; i<=N; i++){
        if (dist1[i]+dist2[i]<T) ans = max(ans, val[i]);
    }
    cout << ans << "\n";
}