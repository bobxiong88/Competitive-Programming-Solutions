// this dude carried: https://robert1003.github.io/2020/01/16/centroid-decomposition.html#a-hrefhttpwcipegcomproblemioi1112ioi11---racea
#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
using namespace std;
#define mx 100005
#define mp make_pair
#define pi pair<int,int>
int n, m, a, b, ans, t, v, x, res, w, y;
set<pi> adj[mx];
unordered_map<int,pi> dist[mx];
vector<int> temp;
int sz[mx], par[mx];
int dfs(int node, int p){
    sz[node] = 1;
    for (auto v: adj[node]){
        if (v.first == p) continue;
        sz[node] += dfs(v.first, node);
    }
    return sz[node];
}
void dfs2(int node, int p, int c, int a, int b){
    dist[c][node] = mp(a,b);
    for (auto v: adj[node]){
        if (v.first == p) continue;
        int x, y;
        x = a; y = b;
        if (v.second >= a){
            y = a;
            x = v.second;
        }
        else if(v.second > b)
            y = v.second;
        dfs2(v.first, node, c, x, y);
    }
}
int centroid(int node, int p, int s){
    for (auto v: adj[node]){
        if (v.first == p) continue;
        if (sz[v.first] > s/2) return centroid(v.first, node, s);
    }
    return node;
}
void build(int node, int p){
    int s = dfs(node, p);
    int c = centroid(node, p, s);
    //if(p == -1) p = c;
    par[c] = p;
    vector<pi> edge(adj[c].begin(), adj[c].end());
    dfs2(c, p, c, 0, 0);
    for (auto v: edge){
        adj[c].erase(v);
        adj[v.first].erase(mp(c,v.second));
        build(v.first, c);
    }
}
int main(){
    //ifstream cin("data.txt");
    //ofstream cout("out.txt");
    ios_base::sync_with_stdio(false); cin.tie(0); //cout.tie(0);
    cin >> n;
    for (int i = 0; i<n-1; i++){
        cin >> a >> b >> w;
        adj[a].insert(mp(b,w));
        adj[b].insert(mp(a,w));
    }
    build(1, 0);
    cin >> m;
    for (int i = 0; i<m; i++){
        cin >> x >> y;
        for (int node = x; node != 0; node = par[node]){
            if (dist[node].count(y)){
                temp.clear();
                temp.push_back(dist[node][x].first); temp.push_back(dist[node][x].second);
                temp.push_back(dist[node][y].first);temp.push_back(dist[node][y].second);
                sort(temp.begin(), temp.end());
                reverse(temp.begin(),temp.end());
                cout << (!temp[1] ? -1 : temp[1]) << "\n";
                break;
            }
        }
    }
}