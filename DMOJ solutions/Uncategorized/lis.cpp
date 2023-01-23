#include<bits/stdc++.h>
using namespace std;
// credit to cp-algorithms.com, im just sorta practicing please no kill
int main(){
    int N;
    cin >> N;
    int a[N];
    int mx = 1e9;
    vector <int> dp(N+1, mx);
    for (int i = 0; i<N; i++){
        cin >> a[i];
    }
    dp[0] = -mx;
    for (int i = 0; i<N; i++){
        int j = upper_bound(dp.begin(), dp.end(), a[i])-dp.begin();
        if (dp[j-1] < a[i] && a[i]<dp[j]) dp[j] = a[i];
    }
    int ans = 0;
    for (int i = 0; i<=N; i++){
        if (dp[i] < mx) ans = i;
    }
    cout << ans;
}