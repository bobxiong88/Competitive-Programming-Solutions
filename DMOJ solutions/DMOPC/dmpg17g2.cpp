// geeks for geeks https://www.geeksforgeeks.org/range-query-largest-sum-contiguous-subarray/
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define pb push_back
#define pii pair<int,int>
#define mx 100005
struct node{
    int sum, pre, suf, maxsum;
};
vector<node> t(mx*4);
void update(int n, int l, int r, int x, int v){
    if (l == r){
        t[n].sum = v;
        t[n].pre = v;
        t[n].suf = v;
        t[n].maxsum = v;
        return;
    }
    int mid = (l+r)/2;
    if (x <= mid)
        update(2*n, l, mid, x, v);
    else
        update(2*n+1, mid+1, r, x, v);
    t[n].sum = t[2*n].sum + t[2*n+1].sum;
    t[n].pre = max(t[2*n].pre, t[2*n].sum + t[2*n+1].pre);
    t[n].suf = max(t[2*n+1].sum + t[2*n].suf, t[2*n+1].suf);
    t[n].maxsum = max(t[n].pre,
                  max(t[n].suf,
                  max(t[2*n].maxsum,
                  max(t[2*n+1].maxsum,
                  t[2*n].suf+t[2*n+1].pre))));
}
node query(int n, int l, int r, int a, int b){
    node res;
    res.sum = res.pre = res.suf = res.maxsum = -1e15;
    if (b < l || r < a) return res;
    if (a <= l && r <= b) return t[n];
    int mid = (l+r)/2;
    if (l > mid)
        return query(2*n+1, mid+1, r, a, b);
    if (r <= mid)
        return query(2*n, l, mid, a, b);
    node left = query(2*n, l, mid, a, b);
    node right = query(2*n+1, mid+1, r, a, b);
    res.sum = left.sum+right.sum;
    res.pre = max(left.pre, left.sum+right.pre);
    res.suf = max(right.suf, right.sum+left.suf);
    res.maxsum = max(res.pre,
                 max(res.suf,
                 max(left.maxsum,
                 max(right.maxsum,
                 left.suf+right.pre))));
    return res;
}
main(){
    for (int i = 0; i<mx*4; i++){
        t[i].sum = -1e15;
        t[i].pre = -1e15;
        t[i].suf = -1e15;
        t[i].maxsum = -1e15;
    }
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, a, b;
    char t;
    cin >> N >> Q;
    for (int i = 1; i<=N; i++){
        cin >> a;
        update(1, 1, N, i, a);
    }
    while (Q--){
        cin >> t >> a >> b;
        if (t == 'S') update(1, 1, N, a, b);
        else{
            int ans = query(1,1,N,a,b).maxsum;
            cout << ans << "\n";
        }
    }
}