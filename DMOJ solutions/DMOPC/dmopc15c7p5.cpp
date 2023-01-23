#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
#define mx 200001
#define inf 2000000000
int N, r, a, b, idx, node, d, n, Q, c, temp, lca;
int tour[mx*2-1] = {0};
bool vis[mx+1] = {false};
int dist[mx+1] = {0};
int heights[mx*2-1];
int first[mx+1];
vector <vector<int>> freq(mx);
vector <vector<int>> adj(mx);
int t[4*mx][2];
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
void build() {
    for (int i = n - 1; i > 0; --i) {
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
int query(int a, int b){
    int l = min(first[a], first[b]);
    int r = max(first[a], first[b]);
    r++;
    int mn = heights[l];
    int res = tour[l];
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
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
int s1(int r, int i){
    int left = 0;
    int right = freq[i].size()-1;
    if (freq[i][right] <= r){
        return freq[i][right];
    }
    while (left <= right){
        int middle = (left + right)/2;
        if (freq[i][middle] <= r && r <= freq[i][middle+1]){
            return freq[i][middle];
        }
        if (freq[i][middle] < r){
            left = middle + 1;
        }
        else{
            right = middle - 1;
        }
    }
}
int s2(int l, int i){
    int left = 0;
    int right = freq[i].size()-1;
    if (freq[i][left] >= l){
        return freq[i][left];
    }
    while (left <= right){
        int middle = (left + right)/2;
        if ( freq[i][middle-1] < l && l <= freq[i][middle]){
            return freq[i][middle];
        }
        if (freq[i][middle] < l){
            left = middle + 1;
        }
        else{
            right = middle - 1;
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);
    fill_n(dist, mx+1, inf);
    fill_n(first, mx+1, inf);
    cin >> N;
    r = 1;
    for (int i = 1; i<=N; i++){
        cin >> c;
        for (int j = 0; j<c; j++){
            cin >> temp;
            adj[i].push_back(temp);
        }
    }
    idx = -1;
    euler(r);
    queue <pair<int,int>> que;
    que.push(make_pair(r, 1));
    dist[r] = 1;
    while (!que.empty()){
        node = que.front().first;
        d = que.front().second;
        que.pop();
        for (auto v: adj[node]){
            if (dist[v] > d+1){
                dist[v] = d+1;
                que.push(make_pair(v, d+1));
            }
        }
    }
    for (int i = 0; i<mx; i++){
        heights[i] = dist[tour[i]];
        first[tour[i]] = min(i, first[tour[i]]);
    }
    n = mx*2-1;
    for (int i = 0; i<n; i++) freq[tour[i]].push_back(i);
    for (int i = 0; i<2*n+2; i++){
        t[i][0] = inf;
        t[i][1] = -1;
    }
    for (int i = 0; i<n; i++){
        t[n+i][0] = heights[i];
        t[n+i][1] = tour[i];
    }
    build();
    cin >> Q;
    for (int i = 0; i<Q; i++){
        cin >> a >> b;
        lca = query(a,b);
        if (first[b] > first[a]){
            cout << first[b] - first[lca] - (heights[first[a]] - heights[first[lca]]) << "\n";
        }
        else if(first[b] == first[a]){
            cout << "0\n";
        }
        else {
            int start = s1(first[a], lca);
            int endd = s2(first[a], lca);
            int diff = endd - start;
            cout << first[b] - first[lca] + diff - (heights[first[a]] - heights[first[lca]]) << "\n";
        }
    }
}