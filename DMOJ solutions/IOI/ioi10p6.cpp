#include <bits/stdc++.h>
using namespace std;
#define M 1000000
vector<vector<int>> adj(M);
int P[M];
int ht[M] = {0};
int dfs(int node, int p, int h){
    ht[node] = h;
    for (auto n: adj[node]){
        if (n == p) continue;
        P[node] += dfs(n, node, h+1);
    }
    return P[node];
}
int LocateCentre(int N, int gay[], int S[], int D[]){
    int s = 0;
    for (int i = 0; i<N; i++){
        P[i] = gay[i];
        s += P[i];
    }
    for (int i = 0; i<N-1; i++){
        adj[S[i]].push_back(D[i]);
        adj[D[i]].push_back(S[i]);
    }
    dfs(0, -1, 0);
    int mx = 2100000000;
    int ans = 0;
    for (int node = 0; node < N; node++){
        int curr = 0;
        for (auto n: adj[node]){
            if (ht[n] < ht[node]) curr = max(curr, s-P[node]);
            else curr = max(curr, P[n]);
        }
        if (curr < mx){
            mx = curr;
            ans = node;
        }
    }
    return ans;
}
int main(){
    //int P[] = {10, 10, 10, 20, 20};
    //int S[] = {0, 1, 3, 4};
    //int D[] = {2, 2, 2, 3};
    //cout << LocateCentre(5, P, S, D);
}