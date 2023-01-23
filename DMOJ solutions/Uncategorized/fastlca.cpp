#include <bits/stdc++.h>
#define N 6000005
using namespace std;
vector<short> h(N, 0);
vector<int> par(N);
short dfs(int i){
    if (h[par[i]]!=0){
        h[i] = h[par[i]]+1;
        if (h[i]>63){
            cout << "cay";
        }
        return h[i];
    }
    return h[i] = dfs(par[i])+1;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int n, Q;
    cin >> n >> Q;
    for (int i = 2; i<=n; i++)
        cin >> par[i];
    h[1] = 1;
    for (int i = 2; i<=n; i++)
        dfs(i);
    while (Q--){
        int a, b;
        cin >> a >> b;
        while(h[a] != h[b]){
            if (h[a] > h[b]) a = par[a];
            else b = par[b];
        }
        while(a != b){
            a = par[a];
            b = par[b];
        }
        cout << a << "\n";
    }
}