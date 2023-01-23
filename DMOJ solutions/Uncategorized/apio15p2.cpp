#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
struct item{
    int node, d;
};
int MAXN = 2000000000;
int N, M, bi, pi, sb, sp, eb;
vector <set<int>> adj(30001);
int dist[30001];
vector <vector<pair<int,int>>> graph(30001);
bool vis[30001] = {false};
int main(){
    cin >> N >> M;
    for (int i = 0; i<M; i++){
        cin >> bi >> pi;
        if (!i) sb = bi;
        if (i==1) eb = bi;
        adj[bi].insert(pi);
    }
    for (int i = 0; i<N; i++) dist[i] = MAXN;
    for (int i = 0; i<N; i++){
        vector<int>temp(adj[i].begin(), adj[i].end());
        sort(temp.begin(), temp.end(), greater <>());
        for (int p: temp){
            for (int j = 1; j*p+i<N; j++){
                if (!vis[j*p+i]){
                    vis[j*p+i] = true;
                    graph[i].push_back(make_pair(j*p+i,j));
                }
                if (adj[i+j*p].count(p)) break;
            }
            for (int j = 1; i-j*p>=0; j++){
                if (!vis[i-j*p]){
                    vis[i-j*p] = true;
                    graph[i].push_back(make_pair(i-j*p,j));
                }
                if (adj[i-j*p].count(p)) break;
            }
        }
        for (auto p:graph[i]) vis[p.first] = false;
    }
    queue <item> que;
    item start = {sb, 0};
    dist[sb] = 0;
    que.push(start);
    while (!que.empty()){
        item curr = que.front(); que.pop();
        if (dist[curr.node] < curr.d) continue;
        for (auto p: graph[curr.node]){
            if (dist[p.first] > curr.d + p.second){
                dist[p.first] = curr.d+p.second;
                item next = {p.first, curr.d+p.second};
                que.push(next);
            }
        }
    }
    if (dist[eb] == MAXN) dist[eb] = -1;
    cout << dist[eb];
}