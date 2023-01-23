#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define mx 2000005
int n;
int h[mx];
int a[mx];
ll t[mx*2];
void modify (int p, ll value) {
    for (t[p += n] = value; p > 1; p >>= 1){
        t[p>>1] = max(t[p], t[p^1]);
    }
}
ll query(int l, int r){
    ll res = 0;
    r++;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = max(res, t[l++]);
        if (r&1) res = max(res, t[--r]);
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i = 1; i<=n; i++)
        cin >> h[i];
    for (int i = 1; i<=n; i++)
        cin >> a[i];
    for (int i = 1; i<=n; i++)
        modify(h[i], a[i]+query(1, h[i]));
    cout << query(1, n);
}