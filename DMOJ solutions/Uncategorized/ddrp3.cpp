#include <bits/stdc++.h>
using namespace std;
int main(){
    int N, M, X, Y, S, T, node, d;
    cin >> N >> M;
    vector<list<int>> adj(N+1);
    for(int i = 0; i<M; i++){
        cin >> X >> Y;
        adj[X].push_back(Y);
        adj[Y].push_back(X);
    }
    cin >> S >> T;
    queue<pair<int,int>>que;
    que.push(make_pair(S,0));
    bool visited[N+1] = {false};
    visited[S] = true;
    while(!que.empty()){
        node = que.front().first;
        d = que.front().second;
        que.pop();
        if(node==T){
            break;
        }
        for(int n: adj[node]){
            if(!visited[n]){
                visited[n] = true;
                que.push(make_pair(n,d+1));
            }
        }
    }
    cout << M-d << "\n";
}