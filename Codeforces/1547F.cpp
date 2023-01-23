#include <bits/stdc++.h>
using namespace std;
#define mx int(8e5)+5
int t[mx*2], a[mx], n, m;
int gcd(int a, int b){
    if (a == 0) return b;
    return gcd(b%a, a);
}
void build(){
    for (int i = m-1; i>0; --i) t[i] = gcd(t[i<<1], t[i<<1|1]);
}
int query(int l, int r){
    r++;
    int res = a[l];
    for (l += m, r += m; l < r; l >>= 1, r >>= 1){
        if (l&1) res = gcd(res, t[l++]);
        if (r&1) res = gcd(res, t[--r]);
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int q;
    cin >> q;
    while (q--){
        cin >> n;
        for (int i = 0; i<n; i++){
            cin >> a[i];
        }
        m = n*2;
        for (int i = 0; i<m; i++){
            t[m+i] = a[i%n];
        }
        build();
        int ans = 0;
        int g = query(0, n-1);
        int res[n];
        //cout << g << "\n";
        for (int i = 0; i<n; i++){
            int l = 0;
            int r = n-1;
            int curr = n-1;
            if (a[i] == g){
                curr = 0;
            }
            else{
                while (l <= r){
                    int mid = (l+r)/2;
                    //cout << i << " "  << i + mid << " " << query(i, i+mid) << "\n";
                    if (query(i, i+mid+1) == g && query(i, i+mid) > g){
                        curr = mid+1;
                        break;
                    }
                    if (query(i, i+mid) > g){
                        l = mid+1;
                    }
                    else{
                        r = mid-1;
                    }
                }
            }

            res[i] = curr;
            ans = max(res[i], ans);
        }
        //for (int i = 0; i<n; i++) cout << res[i] << " "; cout << "\n";
        cout << ans << "\n";
    }
}
