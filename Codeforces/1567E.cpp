#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
const int mx  = int(2e5)+5;
int a[mx];
struct pnt{
    int cnt=0, st=0, ed=0;
};
pnt t[4*mx];
void merge(int tl, int tm, int tr, pnt &curr, pnt &l, pnt &r){
    curr.cnt = l.cnt+r.cnt;
    if (a[tm] <= a[tm+1]){
        curr.cnt += l.ed*r.st;
    }
    curr.st = l.st;
    if (l.st == tm-tl+1 && a[tm] <= a[tm+1]){
        curr.st = l.st+r.st;
    }
    curr.ed = r.ed;
    if (r.ed == tr-tm && a[tm] <= a[tm+1]){
        curr.ed = r.ed+l.ed;
    }
}
void build(int node, int tl, int tr){
    if (tl == tr){
        t[node].cnt = 1;
        t[node].st = 1;
        t[node].ed = 1;
    }
    else{
        int tm = (tl+tr)/2;
        build(node*2, tl, tm);
        build(node*2+1, tm+1, tr);
        merge(tl, tm, tr, t[node], t[node*2], t[node*2+1]);
    }
}
void update(int node, int tl, int tr, int p, int v){
    if (tl == tr){
        a[p] = v;
    }
    else{
        int tm = (tl+tr)/2;
        if (p <= tm) update(node*2, tl, tm, p, v);
        else update(node*2+1, tm+1, tr, p, v);
        merge(tl, tm, tr, t[node], t[node*2], t[node*2+1]);
    }
}
pnt query(int node, int tl, int tr, int l, int r){
    if (tl > tr || tr < l || r < tl) return {0,0,0};
    if (l <= tl && tr <= r) return t[node];
    int tm = (tl+tr)/2;
    pnt curr;
    pnt left = query(node*2, tl, tm, l, r);
    pnt rght = query(node*2+1, tm+1, tr, l, r);
    merge(tl, tm, tr, curr, left, rght);
    return curr;
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int n, q, T, x, y;
    cin >> n >> q;
    for (int i = 1; i<=n; i++) cin >> a[i];
    build(1, 1, n);
    while (q--){
        cin >> T >> x >> y;
        if (T == 1){
            update(1, 1, n, x, y);
        }
        else{
            pnt curr = query(1, 1, n, x, y);
            cout << curr.cnt << "\n";
        }
    }

}
