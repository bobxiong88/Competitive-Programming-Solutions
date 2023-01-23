#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define pii pair<int,int>
#define mx 100005
struct pnt{
    int con, pre, suf, s;
};
int lazy[4*mx];
vector<pnt> t(mx*4);
void lazyUpdate(int node, int tl, int tr){
    if (lazy[node] != -1){
        if (lazy[node] == 0){
            t[node].con = 0;
            t[node].pre = 0;
            t[node].suf = 0;
        }
        else{
            t[node].con = tr-tl+1;
            t[node].pre = tr-tl+1;
            t[node].suf = tr-tl+1;
            t[node].s = tl;
        }
        if (tl != tr){
            lazy[node*2] = lazy[node];
            lazy[node*2+1] = lazy[node];
        }
        lazy[node] = -1;
    }
}
void update(int node, int tl, int tr, int l, int r, int v){
    lazyUpdate(node, tl, tr);
    if (tl > tr || tl > r || l > tr){
        return;
    }
    if (l <= tl && tr <= r){
        if (v == 0){
            t[node].con = 0;
            t[node].pre = 0;
            t[node].suf = 0;
        }
        else{
            t[node].con = tr-tl+1;
            t[node].pre = tr-tl+1;
            t[node].suf = tr-tl+1;
            t[node].s = tl;
        }
        if (tl != tr){
            lazy[node*2]  = v;
            lazy[node*2+1] = v;
        }
        return;
    }
    int mid = (tl+tr)/2;
    update(node*2, tl, mid, l, r, v);
    update(node*2+1, mid+1, tr, l, r, v);

    t[node].pre = t[node*2].pre;
    if (t[node*2].pre==mid-tl+1) t[node].pre += t[node*2+1].pre;

    t[node].suf = t[node*2+1].suf;
    if (t[node*2+1].suf==tr-(mid+1)+1) t[node].suf += t[node*2].suf;

    if (t[node*2].con >= t[node*2+1].con && t[node*2].con >= t[node*2].suf+t[node*2+1].pre){
        t[node].s = t[node*2].s;
    }
    else if (t[node*2].suf+t[node*2+1].pre >= t[node*2].con && t[node*2].suf+t[node*2+1].pre >= t[node*2+1].con){
        t[node].s = mid-t[node*2].suf+1;
    }
    else{
        t[node].s = t[node*2+1].s;
    }
    t[node].con = max(t[node*2].con,
                      max(t[node*2+1].con,
                      t[node*2].suf+t[node*2+1].pre));
}
pnt query(int node, int tl, int tr, int l, int r){
    //cout << "node " << node << " " << tl << " " << tr << "\n";
    pnt res;
    res.con = 0;
    res.pre = 0;
    res.suf = 0;

    if (tl > tr || tl > r || l > tr) return res;
    lazyUpdate(node, tl, tr);
    if (l <= tl && tr <= r) return t[node];

    int mid = (tl+tr)/2;
    pnt left = query(node*2, tl, mid, l, r);
    pnt right = query(node*2+1, mid+1, tr, l, r);

    res.pre = left.pre;
    if (left.pre == mid-tl+1) res.pre += right.pre;

    res.suf = right.suf;
    if (right.suf == tr-(mid+1)+1) res.suf += left.suf;

    if (left.con >= right.con && left.con >= left.suf+right.pre){
        res.s = left.s;
    }
    else if (left.suf+right.pre >= left.con && left.suf+right.pre >= right.con){
        res.s = mid-left.suf+1;
    }
    else{
        res.s = right.s;
    }

    res.con = max(left.con,
                  max(right.con,
                  left.suf+right.pre));
    return res;
}
int main(){
    for (int i = 0; i<mx*4; i++){
        t[i].con = 0;
        t[i].suf = 0;
        t[i].pre = 0;
        lazy[i] = -1;
    }
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, T, l, r;
    cin >> N >> Q;
    while (Q--){
        cin >> T;
        if (T == 2){
            pnt res = query(1, 1, N, 1, N);
            update(1, 1, N, res.s, res.s+res.con-1, 0);
        }
        else{
            cin >> l >> r;
            update(1, 1, N, l, r, T);
            cout << query(1, 1, N, 1, N).con << "\n";
        }
    }
}