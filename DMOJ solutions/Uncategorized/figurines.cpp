#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx int(1e6)+5
#define inf int(3e18)
int a[mx], b[mx];
struct pnt{
    int b, ba, bb;
};
struct lz{
    int ua, ub;
};
pnt t[4*mx];
lz lazy[4*mx];
void build(int node, int tl, int tr){
    if (tl == tr){
        t[node].ba = a[tl];
        t[node].bb = b[tl];
        t[node].b = a[tl]+b[tl];
    }
    else{
        int mid = (tl+tr)/2;
        build(node*2, tl, mid);
        build(node*2+1,mid+1,tr);
        t[node].ba = max(t[node*2].ba, t[node*2+1].ba);
        t[node].bb = max(t[node*2].bb, t[node*2+1].bb);
        t[node].b = max(t[node*2].b, t[node*2+1].b);
    }
}
void lazyUpdate(int node, int tl, int tr){
    if (lazy[node].ua != -inf){
        t[node].ba = lazy[node].ua;
        t[node].b = lazy[node].ua+max(t[node].bb, lazy[node].ub);
        if (tl != tr){
            lazy[node*2].ua = lazy[node].ua;
            lazy[node*2+1].ua = lazy[node].ua;
        }
        lazy[node].ua = -inf;
    }
    if (lazy[node].ub != -inf){
        t[node].bb = max(t[node].bb, lazy[node].ub);
        t[node].b = max(t[node].ba+lazy[node].ub, t[node].b);
        if (tl != tr){
            lazy[node*2].ub = max(lazy[node].ub, lazy[node*2].ub);
            lazy[node*2+1].ub = max(lazy[node].ub, lazy[node*2+1].ub);
        }
        lazy[node].ub = -inf;
    }
}
void make(int node, int tl, int tr, int l, int r, int k){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr) return;
    if (l <= tl && tr <= r){
        t[node].ba = k;
        t[node].b = k+t[node].bb;
        if (tl != tr){
            lazy[node*2].ua = k;
            lazy[node*2+1].ua = k;
        }
        return;
    }
    int mid = (tl+tr)/2;
    make(node*2, tl, mid, l, r, k);
    make(node*2+1,mid+1,tr, l, r, k);
    t[node].bb = max(t[node*2].bb, t[node*2+1].bb);
    t[node].ba = max(t[node*2].ba, t[node*2+1].ba);
    t[node].b = max(t[node*2].b,t[node*2+1].b);
}
void maximize(int node, int tl, int tr, int l, int r, int k){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr) return;
    if (l <= tl && tr <= r){
        t[node].bb = max(t[node].bb,k);
        t[node].b = max(t[node].ba+k, t[node].b);
        if (tl != tr){
            lazy[node*2].ub = max(k, lazy[node*2].ub);
            lazy[node*2+1].ub = max(k, lazy[node*2+1].ub);
        }
        return;
    }
    int mid = (tl+tr)/2;
    maximize(node*2, tl, mid, l, r, k);
    maximize(node*2+1,mid+1,tr, l, r, k);
    t[node].bb = max(t[node*2].bb, t[node*2+1].bb);
    t[node].ba = max(t[node*2].ba, t[node*2+1].ba);
    t[node].b = max(t[node*2].b,t[node*2+1].b);
}
int query(int node, int tl, int tr, int l, int r){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr) return -inf;
    if (l <= tl && tr <= r) return t[node].b;
    int mid = (tl+tr)/2;
    return max(query(node*2, tl, mid, l, r), query(node*2+1, mid+1,tr, l, r));
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    for (int i = 0; i<4*mx; i++){
        lazy[i].ua = -inf;
        lazy[i].ub = -inf;
    }
    int N, Q, q, l, r, k;
    cin >> N >> Q;
    for (int i = 1; i<=N; i++){
        cin >> a[i];
    }
    for (int i = 1; i<=N; i++){
        cin >> b[i];
    }
    build(1, 1, N);
    while (Q--){
        cin >> q;
        if (q==1){
            cin >> l >> r >> k;
            make(1, 1, N, l, r, k);
        }
        else if(q==2){
            cin >> l >> r >> k;
            maximize(1, 1, N, l, r, k);
        }
        else{
            cin >> l >> r;
            cout << query(1, 1, N, l, r) << "\n";
        }
    }
}