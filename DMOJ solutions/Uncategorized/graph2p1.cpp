#include <bits/stdc++.h>
using namespace std;
vector<vector<int>>adj(1001);
int N, a;
bool vis[1001] = {false};
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for (int i = 1; i<=N; i++){
        for (int j = 1; j<=N; j++){
            cin >> a;
            if (a)
                adj[i].push_back(j);
        }
    }
    for (int i = 1; i<=N; i++){
        if (!vis[i]){
            queue <int> que;
            vector<int> path;
            que.push(i);
            vis[i] = true;
            path.push_back(i);
            while(!que.empty()){
                int node = que.front(); que.pop();
                for (int n: adj[node]){
                    if (!vis[n]){
                        path.push_back(n);
                        vis[n] = true;
                        que.push(n);
                    }
                }
            }
            sort(path.begin(), path.end());
            for (int i:path)
                cout << i << " ";
            cout << "\n";
        }

    }
}