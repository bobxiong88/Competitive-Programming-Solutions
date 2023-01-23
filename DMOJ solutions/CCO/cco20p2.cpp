#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll

#define mx int(2e5)+5
int bit[mx], t[4*mx];
int lsb(int x){
    return x&(-x);
}
int query(int x){
    int res = 0;
    for (int i = x; i>0; i-=lsb(i))
        res += bit[i];
    return res;
}
void upd(int x, int v){
    for (int i = x; i<mx; i+=lsb(i))
        bit[i] += v;
}
int qa(int l, int r){
    return query(r)-query(l-1);
}
void update(int node, int tl, int tr, int x, int v){
    if (tl == tr){
        t[node] = v;
    }
    else{
        int mid  = (tl+tr)/2;
        if (x <= mid) update(node*2, tl, mid, x, v);
        else update(node*2+1, mid+1, tr, x, v);
        t[node] = max(t[node*2], t[node*2+1]);
    }
}
int query(int node, int tl, int tr, int v){
    if (t[node] < v) return -1;
    if (tl == tr) return tl;
    int mid = (tl+tr)/2;
    int right = query(node*2+1, mid+1, tr, v);
    if (right !=-1) return right;
    return query(node*2, tl, mid, v);
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, ans;
    cin>> N;
    int d[N+1];
    int tar[N+1];
    for (int i = 1;i<=N; i++){
        cin >> d[i];
        update(1, 1, N, i, d[i]);
    }
    for (int i = N; i>=1; i--){
        int res = query(1, 1, N, i);
        if (res == -1){
            cout << -1;
            return 0;
        }
        tar[res] = i;
        update(1, 1, N, res, 0);
    }
    ans = 0;
    for (int i = 1; i <= N; i++){
        upd(tar[i], 1);
        ans += qa(tar[i]+1, N);
    }
    cout << ans;
}