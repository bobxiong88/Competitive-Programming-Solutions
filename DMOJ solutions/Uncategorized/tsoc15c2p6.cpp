#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx int(3e6)+5
int arr[mx], t[mx*4], lazy[mx*4];
void lazyUpdate(int node, int tl, int tr){
    if (lazy[node]){
        t[node] -= lazy[node];
        if (tl != tr){
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
void build(int node, int tl, int tr){
    if (tl == tr){
        t[node] = arr[tl];
    }
    else{
        int tm = (tl+tr)/2;
        build(2*node, tl, tm);
        build(2*node+1, tm+1, tr);
        t[node] = min(t[node*2], t[node*2+1]);
    }
}
void update(int node, int tl, int tr, int l, int r, int v){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr || tl > tr) return;
    if (l <= tl && tr <= r){
        t[node] -= v;
        if (tl != tr){
            lazy[node*2] += v;
            lazy[node*2+1] += v;
        }
        return;
    }
    int tm = (tl+tr)/2;
    update(node*2, tl, tm, l, r, v);
    update(node*2+1,tm+1,tr, l, r, v);
    t[node] = min(t[node*2], t[node*2+1]);
}
int query(int node, int tl, int tr, int l, int r){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr || tl > tr) return int(1e18);
    if (l <= tl && tr <= r) return t[node];
    int tm = (tl+tr)/2;
    return min(query(node*2, tl, tm, l, r), query(node*2+1, tm+1, tr, l, r));
}
main(){
    //ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, a, b, c;

    cin >> N >> Q;
    if (N>1000000){
        return 0;
    }
    for (int i = 1; i<=N; i++) cin >> arr[i];
    build(1,1,N);
    while (Q--){
        cin >> a >> b >> c;
        update(1, 1, N, a, b, c);
        cout << max((ll)0, query(1, 1, N, a, b)) << " " << max((ll)0, t[1]) << "\n";
    }
}