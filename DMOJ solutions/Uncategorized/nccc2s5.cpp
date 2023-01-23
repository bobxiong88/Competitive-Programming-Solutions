#include <bits/stdc++.h>
using namespace std;
struct edge{
    int a, b, w;
};
int n, M, Q, u, v, z, q, a, b, node, p, c, w, nr;
vector <edge> edges;
vector <vector<pair<int,int>>> graph(1001);
int parent[1001];
int s[1001];
bool comp(const edge &a, const edge &b){
    return a.w > b.w;
}
int f(int v){
    if (v == parent[v]) return v;
    return parent[v] = f(parent[v]);
}
void join(int a, int b){
    a = f(a);
    b = f(b);
    if (a != b){
        if (s[a] < s[b]) swap(a,b);
        parent[b] = a;
        s[a] += s[b];
    }
}
void build(int m, int x){
    edges[m].w = x;
    vector <edge> sorted = edges;
    sort(sorted.begin(), sorted.end(), comp);
    int c = 0;
    for (edge e: sorted){
        if (c >= n) break;
        if (f(e.a) != f(e.b)){
            c++;
            join(e.a, e.b);
            graph[e.a].push_back(make_pair(e.b, e.w));
            graph[e.b].push_back(make_pair(e.a, e.w));
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);
    cin >> n >> M;
    edges.push_back(edge({0,0,0}));
    for (int i = 0; i < M; i++){
        cin >> u >> v >> z;
        edges.push_back(edge({u, v, z}));
    }
    for (int i = 0; i<1001; i++){
        parent[i] = i;
        s[i] = 1;
    }
    build(0,0);
    cin >> Q;
    for (int i = 0; i < Q; i++){
        cin >> q;
        if (q == 1){
            cin >> a >> b;
            for (int i = 0; i < 1001; i++){
                parent[i] = i;
                s[i] = 1;
                graph[i].clear();
            }
            build(a,b);
        }
        else{
            cin >> a >> b >> w;
            queue <pair<int,int>> que;
            que.push(make_pair(a, -1));
            int ans = 0;
            while (!que.empty()){
                node = que.front().first;
                p = que.front().second;
                que.pop();
                if (node == b){
                    ans = 1;
                    break;
                }
                for (auto e: graph[node]){
                    nr = e.first;
                    c = e.second;
                    if (nr != p){
                        if (c >= w){
                            que.push(make_pair(nr,node));
                        }
                    }
                }
            }
            cout << ans << "\n";
        }
    }
}