#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx 1000005
int size[mx][2];
int parent[mx];
int find(int v){
    if (v == parent[v]) return v;
    return parent[v] = find(parent[v]);
}
void join(int a, int b){
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (size[a][0] < size[b][0]) swap(a,b);
    size[a][0] += size[b][0];
    size[a][1] += size[b][1];
    parent[b] = a;
}
int n, q, Q, a, b;
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> Q;
    for(int i = 1; i<=n; i++){
        cin >> size[i][1];
        size[i][0] = 1;
        parent[i] = i;
    }
    for(int i = 0; i<Q;i++){
        cin >> q;
        if (q == 1){
            cin >> a >> b;
            join(a,b);
        }
        else if (q == 2){
            cin >> a;
            cout << size[find(a)][0] << "\n";
        }
        else{
            cin >> a;
            cout << size[find(a)][1] << "\n";
        }
    }
}