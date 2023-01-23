#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define mx 100005
typedef tree<
    int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update
    >
ost;
int N, M, x, Q, a, b;
int student[mx], par[mx], sz[mx];
map<int, ost> group;
char q;
int leader(int v){
    if (par[v] == v) return v;
    return par[v] = leader(par[v]);
}
void join(int a, int b){
    a = leader(a); b = leader(b);
    if (a == b) return;
    if (sz[a] < sz[b]) swap(a, b);
    for (int i = 0; i<group[b].size(); i++){
        group[a].insert(*group[b].find_by_order(i));
    }
    sz[a] += sz[b];
    par[b] = a;

}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> M;
    for (int i = 1; i<=N; i++){
        cin >> x;
        student[x] = i;
        group[i].insert(x);
        par[i] = i;
        sz[i] = 1;
    }
    while(M--){
        cin >> a >> b;
        join(a, b);
    }
    cin >> Q;
    while (Q--){
        cin >> q >> a >> b;
        if (q == 'Q'){
            a = leader(a);
            if (b > group[a].size()) cout << -1 << "\n";
            else cout << student[*group[a].find_by_order(b-1)] << "\n";
        }
        else join(a, b);
    }
    return 0;
}