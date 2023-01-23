#include <bits/stdc++.h>
using namespace std;
int dp[32];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, x;
    cin >> N;
    for (int i = 0; i<N; i++){
        cin >> x;
        int res = 1;
        for (int j = 0; j<32; j++){
            if ((x>>j)&1){
                res = max(res, dp[j]+1);
            }
        }
        for (int j = 0; j<32; j++){
            if ((x>>j)&1){
                dp[j] = max(dp[j], res);
            }
        }
    }
    int ans = 1;
    for (int i = 0; i<32; i++){
        ans = max(ans, dp[i]);
    }
    cout << ans;
}