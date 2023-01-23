#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> dp(n,1);
    int ans = 0;
    for(int i = 0;i<n;i++) cin >> a[i];
    for(int i = 0;i<n;i++){
        for(int j = 0; j<i; j++){
            if (a[j] < a[i])
                dp[i] = max(dp[j]+1, dp[i]);
        }
        ans = max(ans, dp[i]);
    }
    cout << ans;
}