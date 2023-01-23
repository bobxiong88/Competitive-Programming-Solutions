#include <bits/stdc++.h>
using namespace std;
#define mx int(2e5)+5
#define inf int(1e9)
int bk[mx], t[4*mx], lazy[4*mx], val[mx];
void lazyUpdate(int node, int tl, int tr){
    if (lazy[node]){
        t[node] += lazy[node];
        if (tl != tr){
            lazy[2*node] += lazy[node];
            lazy[2*node+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
void update(int node, int tl, int tr, int l, int r, int v){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr || l > r) return;
    if (l <= tl && tr <= r){
        t[node] += v;
        if (tl != tr){
            lazy[2*node] += v;
            lazy[2*node+1] += v;
        }
        return;
    }
    int tm = (tl+tr)/2;
    update(2*node, tl, tm, l, r, v);
    update(2*node+1, tm+1, tr, l, r, v);
    t[node] = min(t[node*2], t[node*2+1]);
}
int query(int node, int tl, int tr, int l, int r){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr || l > r) return inf;
    if (l <= tl && tr <= r) return t[node];
    int tm = (tl+tr)/2;
    return min(query(2*node, tl, tm, l, r), query(2*node+1, tm+1, tr, l, r));
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M, a, b;
    cin >> N >> M;
    for (int i = 0;i<N; i++){
        bk[i] = i;
    }
    while(M--){
        cin >> a >> b;
        a--; b--;
        bk[max(a,b)] = min(bk[max(a,b)],min(a,b));
    }
    val[0] = 0;
    multiset<int> pog;
    for (int i = 2; i<N; i++) pog.insert(bk[i]);
    for (int i = 1; i<N; i++){
        if (i != 1) pog.erase(pog.find(bk[i]));
        int mn = i;
        if (!pog.empty()){
            mn = min(mn, *pog.begin());
        }
        if (bk[i]-1 >= 0) update(1, 0, N-1, 0, bk[i]-1, 1);
        if (mn-1 >= 0) val[i] = query(1, 0, N-1, 0, mn-1);
        else val[i] = inf;
        update(1, 0, N-1, i, i, val[i]);
    }
    cout << query(1, 0, N-1, N-1, N-1);
}