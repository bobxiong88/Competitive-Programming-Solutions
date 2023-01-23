#include <bits/stdc++.h>
using namespace std;
#define mx 400005
int N, M, K, a, b, v, curr;
int par[mx], sz[mx];
bool mark[mx];
vector<int> ans, vr;
vector<pair<int,int>> edges;
vector<int> adj[mx];
set<int> arr;
int leader(int v){
    if (par[v] == v) return v;
    return leader(par[v]);
}
bool join(int a, int b){
    a = leader(a); b = leader(b);
    if (a == b) return false;
    if (sz[a] < sz[b]) swap(a,b);
    par[b] = a;
    sz[a] += sz[b];
    return true;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    for (int i = 0; i<mx; i++){
        par[i] = i;
        sz[i] = 1;
        mark[i] = true;
    }
    cin >> N >> M;
    for (int i = 0; i<M; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        edges.push_back(make_pair(a,b));
    }
    cin >> K;
    while(K--){
        cin >> v;
        mark[v] = false;
        vr.push_back(v);
    }
    for (auto [a,b]: edges){
        if (mark[a] && mark[b]) join(a,b);
    }
    for (int i = 0; i<N; i++){
        if (mark[i]) arr.insert(leader(i));
    }
    ans.push_back(arr.size());
    reverse(vr.begin(), vr.end());
    for (auto n: vr){
        curr = ans[ans.size()-1];
        if(!mark[n]){
            curr++;
            mark[n] = true;
        }
        for (auto v:adj[n]){
            if (mark[v]){
                if (join(n, v)){
                    curr--;
                }
            }
        }
        ans.push_back(curr);
    }
    reverse(ans.begin(), ans.end());
    for (auto k:ans){
        cout << k << "\n";
    }
}