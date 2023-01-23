// this dude carried: https://robert1003.github.io/2020/01/16/centroid-decomposition.html#a-hrefhttpwcipegcomproblemioi1112ioi11---racea
#include <bits/stdc++.h>
using namespace std;
#define mx 400005
#define pi pair<int,int>
#define mp make_pair
#define pb push_back
#define mm 2000005
int n, a, b, w, res, ans, k, idx, tot;
set<pi> adj[mx];
vector<int> graph[mx];
vector<int> balls;
vector<int> fatballs;
bool vis[mx];
int sz[mx], cnt[mm], heights[mx], first[mx], tour[mx*2], dist[mx], par[mx], diff[mx];
int t[mx*4][2];
bool gay;
void buildtree() {
    for (int i = mx*2-1; i > 0; --i) {
        if (t[i<<1][0] <= t[i<<1|1][0]) {
            t[i][0] = t[i<<1][0];
            t[i][1] = t[i<<1][1];
        }
        else {
            t[i][0] = t[i<<1|1][0];
            t[i][1] = t[i<<1|1][1];
        }
    }
}
int lca(int a, int b){
    int l = min(first[a], first[b]);
    int r = max(first[a], first[b]);
    r++;
    int mn = heights[l];
    int res = tour[l];
    for (l += mx*2, r += mx*2; l < r; l >>= 1, r >>= 1) {
        if (l&1){
            if (t[l][0] < mn){
                mn = t[l][0];
                res = t[l][1];
            }
            l++;
        }
        if (r&1){
            r--;
            if (t[r][0] < mn){
                mn = t[r][0];
                res = t[r][1];
            }
        }
    }
    return res;
}
void update(int a, int b, int v){
    int c = lca(a,b);
    if (c == a){
        diff[b] += v;
        if (!(c==1 && par[c]==1)) diff[par[c]]-=v;
    }
    else if(c == b){
        diff[a] += v;
        if (!(c==1 && par[c]==1)) diff[par[c]]-=v;
    }
    else{
        diff[a]+=v;
        diff[b]+=v;
        if (!(c==1 && par[c]==1)) diff[par[c]]-=v;
        diff[c]-=v;
    }
}
int dfs(int node, int p){
    sz[node] = 1;
    for (auto v: adj[node]){
        if (v.first == p) continue;
        sz[node] += dfs(v.first, node);
    }
    return sz[node];
}
void dfs2(int node, int p, int c, int cost){
    int get = k-cost;
    if (get < 0) return;
    if (cnt[get]>0){
        update(c, node, cnt[get]);
        if (gay) {
            update(c, c, -cnt[get]);
        }
        else{
            tot += cnt[get];
        }
    }
    balls.pb(cost);
    fatballs.pb(cost);
    for (auto v: adj[node]){
        if (v.first == p) continue;
        dfs2(v.first, node, c, cost + v.second);
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
    vector<pi> edge(adj[c].begin(), adj[c].end());
    cnt[0] = 1;

    gay = false;
    fatballs.clear();
    for (auto v: edge){
        balls.clear();
        dfs2(v.first, c, c, v.second);
        for (int bruh: balls){
            cnt[bruh]++;
        }
    }

    for (auto i: fatballs)
        cnt[i] = 0;

    cnt[0] = 0;
    balls.clear();
    reverse(edge.begin(), edge.end());
    gay = true;
    fatballs.clear();
    for (auto v: edge){
        balls.clear();
        dfs2(v.first, c, c, v.second);
        for (int bruh: balls){
            cnt[bruh]++;
        }
    }
    for (auto i: fatballs)
        cnt[i] = 0;

    for (auto v: edge){
        adj[c].erase(v);
        adj[v.first].erase(mp(c, v.second));
        build(v.first, c);
    }
}
void tree(int node, int p){
    dist[node] = dist[p]+1;
    par[node] = p;
    for (auto v: graph[node]){
        if (v == p) continue;
        tree(v, node);
    }
}
void euler(int u){
    vis[u] = true;
    idx++;
    tour[idx] = u;
    for (auto v: graph[u]){
        if(!vis[v]){
            euler(v);
            idx++;
            tour[idx] = u;
        }
    }
}
void kms(int node, int p){
    for (int v: graph[node]){
        if (v == p) continue;
        kms(v, node);
        diff[node] += diff[v];
    }
}
int gcd(int a, int b){
    if (a == 0) return b;
    return gcd(b%a, a);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> n >> k;
    for (int i = 0; i<n-1; i++){
        cin >> a >> b >> w;
        adj[a].insert(mp(b,w));
        adj[b].insert(mp(a,w));
        graph[a].pb(b);
        graph[b].pb(a);
    }
    for (int i = 0; i<mx*4; i++){
        t[i][0] = 1e9;
        t[i][1] = -1;
    }
    fill_n(first, mx, 1e9);
    tree(1, 1);
    idx = -1;
    euler(1);
    for (int i = mx*2-1; i>=0; i--){
        heights[i] = dist[tour[i]];
        first[tour[i]] = i;
    }
    for (int i = 0; i<mx*2; i++){
        t[mx*2+i][0] = heights[i];
        t[mx*2+i][1] = tour[i];
    }
    buildtree();
    build(1, 1);
    kms(1,1);
    for (int i = 1; i<=n; i++){
        if (tot == 0)
            cout << "0 / 1\n";
        else
            cout << diff[i]/gcd(diff[i], tot) << " / " << tot/gcd(diff[i], tot) << "\n";
    }
}