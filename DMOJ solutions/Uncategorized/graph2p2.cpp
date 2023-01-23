#include <bits/stdc++.h>
using namespace std;
vector <vector<int>> adj(1000);
bool st[1000] = {false};
bool vis[1000] = {false};
bool cycle(int node){
    vis[node] = true;
    st[node] = true;
    for (int n: adj[node]){
        if (!vis[n]){
            if (cycle(n)){
                return true;
            }
        }
        else if (st[n]){
            return true;
        }
    }
    st[node] = false;
    return false;
}
int main(){
    cin.tie(0)->sync_with_stdio(0);
    int n,x, c;
    cin >> n;
    for (int i = 0; i<n; i++){
        for (int j = 0; j<n; j++){
            cin >> x;
            if (x)  adj[i].push_back(j);
        }
    }
    for (int node = 0; node<n; node++){
        if (!vis[node]){
            if (cycle(node)){
                cout << "NO";
                return 0;
            }
        }
    }
    cout << "YES";

}