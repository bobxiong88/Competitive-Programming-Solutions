#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
const int mx = int(2e6)+5;
const int N = int(1e6)+5;
struct v{
    int sum, ed;
};
v t[4*mx];
v merge(v a, v b){
    return {a.sum+b.sum, max(a.ed+b.sum, b.ed)};
}
void build(int node, int tl, int tr){
    if (tl == tr){
        t[node].sum = 0;
        t[node].ed = tl;
    }
    else {
        int tm = (tl+tr)/2;
        build(node*2, tl, tm); build(node*2+1, tm+1, tr);
        t[node] = merge(t[node*2], t[node*2+1]);
    }
}
void update(int node, int tl, int tr, int p, int x){
    if (tl == tr){
        t[node].sum += x;
        t[node].ed += x;
    }
    else{
        int tm = (tl+tr)/2;
        if (p <= tm) update(node*2, tl, tm, p, x);
        else update(node*2+1, tm+1, tr, p, x);
        t[node] = merge(t[node*2], t[node*2+1]);
    }
}
v query(int node, int tl, int tr, int l, int r){
    if (tl > r || tr < l) return {0,0};
    if (l <= tl && tr <= r) return t[node];
    int tm = (tl+tr)/2;
    return merge(query(node*2, tl, tm, l, r), query(node*2+1, tm+1, tr, l, r));
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    for (int i = 0; i<4*mx; i++) t[i] = {0,0};
    int Q;
    char q;
    cin >> Q;
    vector<pii> k;
    int time, d, i;
    build(1, 1, N);
    while (Q--){
        cin >> q;
        if (q == '+'){
            cin >> time >> d;
            update(1, 1, N, time, d);
            k.pb(mp(time, d));
        }
        else if (q == '-'){
            cin >> i;
            update(1, 1, N, k[i-1].first, -k[i-1].second);
            k.pb(mp(1,1));
        }
        else{
            cin >> time;
            v res = query(1, 1, N, 1, time);
            //cout << res.sum << " " << res.ed << "\n";
            cout << res.ed-time << "\n";
            k.pb(mp(1,1));
        }
    }
}
