#include <bits/stdc++.h>
using ll = long long;
#define int ll
using namespace std;
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cout.tie(0);
    int n,k;
    cin >> n >> k;
    vector<int> a(n);
    vector<int> curr(n, 1);
    for(int i = 0; i<n; i++){
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    int ans = 0;
    int mod = 1e9+7;
    for(int x = 0; x < k-1; x++){
        for(int i = 0; i<n-x-1; i++){
            curr[i+1] = (curr[i+1]+curr[i])%mod;
        }
    }
    for(int i = 0; i<n-k+1; i++){
        ans += (curr[i]*a[i+k-1])%mod;
        ans %= mod;
    }
    cout << ans;
    return 0;
}