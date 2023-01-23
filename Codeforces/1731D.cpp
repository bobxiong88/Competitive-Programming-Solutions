#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mp make_pair
#define pb push_back

main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        int m;
        cin >> n >> m;
        int a[n+1][m+1];

        for (int i = 1; i<=n; i++){
            for (int j = 1; j<=m; j++)cin >> a[i][j];
        }
        int l = 1;
        int r = min(n,m);
        int ans = 1;
        while (l<=r){
            int k = (l+r)/2;
            int dp[n+1][m+1];
            for (int i = 0; i<=n; i++){
                dp[i][0] = 0;
            }
            for (int j = 0; j<=m; j++){
                dp[0][j] = 0;
            }
            bool pos = false;
            for (int i = 1; i<=n; i++){
                for (int j = 1; j<=m; j++){
                    if (a[i][j] >= k) dp[i][j] = min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]))+1;
                    else dp[i][j] = 0;
                    if (dp[i][j]>=k){
                        pos = true;
                    }
                }
            }
            if (pos){
                l = k+1;
                ans = max(ans,k);
            }
            else{
                r = k-1;
            }
        }
        cout << ans << "\n";
    }
}
