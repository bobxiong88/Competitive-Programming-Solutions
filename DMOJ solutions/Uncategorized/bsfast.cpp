#include <bits/stdc++.h>
using namespace std;
#define mx 1000010
int a[mx], t[mx*4];
void build(int node, int tl, int tr){
    if (tl == tr){
        t[node] = a[tl];
    }
    else{
        int mid = (tl+tr)/2;
        build(node*2, tl, mid);
        build(node*2+1, mid+1, tr);
        t[node] = min(t[node*2], t[node*2+1]);
    }
}
void update(int node, int tl, int tr, int x, int v){
    if (tl == tr){
        t[node] = v;
    }
    else{
        int mid  = (tl+tr)/2;
        if (x <= mid) update(node*2, tl, mid, x, v);
        else update(node*2+1, mid+1, tr, x, v);
        t[node] = min(t[node*2], t[node*2+1]);
    }
}
int query(int node, int tl, int tr, int l, int k){
    if (t[node] >= k || tr < l) return -1;
    if (tl == tr){
        if (t[node] < k) return tl;
        return -1;
    }
    int mid = (tl+tr)/2;
    int left = query(node*2, tl, mid, l, k);
    if (left !=-1) return left;
    return query(node*2+1, mid+1, tr, l, k);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, T, l, r, k, p, x;
    cin >> N >> Q;
    for (int i = 1; i<=N; i++) cin >> a[i];
    build(1, 1, N);
    int res = 0;
    while (Q--){
        cin >> T;
        if (T == 1){
            cin >> p >> x;
            p ^= res; x ^= res;
            update(1, 1, N, p, x);
        }
        else{
            cin >> l >> r >> k;
            l ^= res; r ^= res; k ^= res;
            res = query(1, 1, N, l, k);
            cout << res << "\n";
        }
    }
}