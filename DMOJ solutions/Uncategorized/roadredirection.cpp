#include <bits/stdc++.h>
using namespace std;
#define mx 400005
#define inf 2000000000
struct road{
    int a,b;
};
int N, r, a, b, idx, node, d, n, Q, q, x;
int tour[mx*2-1] = {0};
bool vis[mx+1] = {false};
int dist[mx+1] = {0};
int heights[mx*2-1];
int first[mx+1];
int last[mx+1];
vector <vector<int>> adj(mx);
vector <road> roads;
int tree[8*mx] = {0};
int lazy[8*mx] = {0};

// used template lazy propagation from hackerearth.com
void euler(int u){
    vis[u] = true;
    idx++;
    tour[idx] = u;
    for (auto v: adj[u]){
        if(!vis[v]){
            euler(v);
            idx++;
            tour[idx] = u;
        }
    }
}
void updateRange(int node, int start, int endd, int l, int r, int val)
{
    if(lazy[node] != 0)
    {
        tree[node] += (endd - start + 1) * lazy[node];
        if(start != endd)
        {
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
    if(start > endd || start > r || endd < l)
        return;
    if(start >= l && endd <= r)
    {
        tree[node] += (endd - start + 1) * val;
        if(start != endd)
        {
            lazy[node*2] += val;
            lazy[node*2+1] += val;
        }
        return;
    }
    int mid = (start + endd) / 2;
    updateRange(node*2, start, mid, l, r, val);
    updateRange(node*2 + 1, mid + 1, endd, l, r, val);
    tree[node] = tree[node*2] + tree[node*2+1];
}
int queryRange(int node, int start, int endd, int l, int r)
{
    if(start > endd || start > r || endd < l)
        return 0;
    if(lazy[node] != 0)
    {

        tree[node] += (endd - start + 1) * lazy[node];
        if(start != endd)
        {
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
    if(start >= l && endd <= r)
        return tree[node];
    int mid = (start + endd) / 2;
    int p1 = queryRange(node*2, start, mid, l, r);
    int p2 = queryRange(node*2 + 1, mid + 1, endd, l, r);
    return (p1 + p2);
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    fill_n(dist, mx+1, inf);
    fill_n(first, mx+1, inf);
    cin >> N >> Q;
    r = 1;
    roads.push_back({0,0});
    for (int i = 0; i<N-1; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        roads.push_back({a,b});
    }
    idx = -1;
    euler(r);
    for (int i = 0; i<mx; i++){
        first[tour[i]] = min(i, first[tour[i]]);
        last[tour[i]] = max(i, last[tour[i]]);
    }
    for (auto e: roads) {
        if (e.a&&e.b){
            if (first[e.a] > first[e.b]){
                if (first[e.a]) {
                    updateRange(1, 0, last[1], 0, first[e.a]-1, 1);
                }
                if (last[e.a]+1<=last[1]){
                    updateRange(1, 0, last[1], last[e.a]+1, last[1], 1);
                }
            }
            else{
                updateRange(1, 0, last[1], first[e.b], last[e.b], 1);
            }
        }
    }
    while (Q--){
        cin >> q >> x;
        if (q == 1){
            cout << queryRange(1, 0, last[1], first[x], first[x]) << "\n";
        }
        else{
            road e = roads[x];
            if (first[e.a] > first[e.b]){
                if (first[e.a])
                    updateRange(1, 0, last[1], 0, first[e.a]-1, -1);
                if (last[e.a]+1<=last[1])
                    updateRange(1, 0, last[1], last[e.a]+1, last[1], -1);
                updateRange(1, 0, last[1], first[e.a], last[e.a], 1);
            }
            else{
                if (first[e.b])
                    updateRange(1, 0, last[1], 0, first[e.b]-1, 1);
                if (last[e.b]+1<=last[1])
                    updateRange(1, 0, last[1], last[e.b]+1, last[1], 1);
                updateRange(1, 0, last[1], first[e.b], last[e.b], -1);
            }
            roads[x] = {e.b, e.a};
        }
    }

}