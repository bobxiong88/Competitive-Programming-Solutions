#include <bits/stdc++.h>
#define int long
using namespace std;
int a[100001];
int t[400004];
void build(int v, int tl, int tr){
    if(tl == tr)
        t[v] = a[tl];
    else{
        int tm = floor((tl + tr))/2;
        build(v*2, tl, tm);
        build(v*2+1, tm+1, tr);
        t[v] = int(t[v*2]&t[v*2+1]);
    }
}
int query(int v, int tl, int tr, int l, int r){
    if (l > r)
        return -1;
    if (l == tl && r == tr)
        return t[v];
    int tm = floor((tl+tr)/2);
    int left = query(v*2, tl, tm, l, min(r, tm));
    int right = query(v*2+1, tm+1, tr, max(l, tm+1), r);
    if (left == -1)
        left = pow(2,32)-1;
    if (right == -1)
        right = pow(2,32)-1;
    return int(left&right);
}
void update(int v, int tl, int tr, int pos, int new_val){
    if (tl == tr)
        t[v] = new_val;
    else{
        int tm = floor((tl+tr)/2);
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = int(t[v*2]&t[v*2+1]);
    }
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N, Q, x, y, val;
    string q;
    cin >> N >> Q;
    for(int i = 1; i<=N; i++) cin >> a[i];
    build(1, 1, N);
    while (Q--){
        cin >> q;
        if (q == "U"){
            cin >> x >> val;
            update(1, 1, N, x, val);
        }
        else{
            cin >> x >> y >> val;
            cout << int(val&query(1, 1, N, x, y)) << "\n";
        }
    }
}