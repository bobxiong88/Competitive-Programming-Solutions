#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
int t[2000002][2]; // min, max
int n, m, c, a;
bool f = false;
void build(){
    for (int i = n - 1; i > 0; --i){
        t[i][0] = min(t[i<<1][0], t[i<<1|1][0]);
        t[i][1] = max(t[i<<1][1], t[i<<1|1][1]);
    }
}
int query(int l, int r){
    r++;
    int mx = -1, mn = 2000000000;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1){
            l++;
            mn = min(t[l-1][0], mn);
            mx = max(t[l-1][1], mx);
        }
        if (r&1){
            --r;
            mn = min(t[r][0], mn);
            mx = max(t[r][1], mx);
        }
    }
    //cout << mx << "|" << mn << "\n";
    return mx-mn;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);
    cin >> n >> m >> c;
    n++;
    for(int i = 1; i<n; ++i){
        cin >> a;
        t[n+i][0] = a;
        t[n+i][1] = a;
    }
    build();
    for (int i = 1; i<=n-m; i++){
        int res = query(i, i+m-1);
        //cout << res << "\n";
        if (res<=c){
            cout << i << "\n";
            f = true;
        }
    }
    if (!f){
        cout << "NONE" << "\n";
    }
}