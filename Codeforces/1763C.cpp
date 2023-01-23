#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i<n; i++) cin >> a[i];
        if (n == 2){
            cout << max(a[0]+a[1], abs(a[0]-a[1])*2) << "\n";
            continue;
        }
        if (n == 3){
            cout << max(a[0]*3,
                        max(a[2]*3,
                            max(abs(a[0]-a[2])*3,
                                max(abs(a[0]+a[1]+a[2]),
                                    max(abs(a[0]-a[1])*2+a[2],
                                        max(abs(abs(a[0]-a[1])-a[2])*3,
                                            max(abs(a[1]-a[2])*2+a[0],
                                                max(abs(abs(a[1]-a[2])-a[0])*3,
                                                    max(abs(a[0]-a[1])*3,abs(a[1]-a[2])*3))))))))) << "\n";
            continue;
        }
        int ans = 0;
        for (int i = 0; i<n; i++){
            ans = max(ans, a[i]*n);
        }
        cout << ans << "\n";
    }
}
