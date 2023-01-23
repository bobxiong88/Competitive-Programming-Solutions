#include <bits/stdc++.h>
using namespace std;
const int mx = pow(2,31);
int main(){
    int N, K;
    cin >> N >> K;
    int X[K][N+1];
    for (int i = 0; i<K; i++){
        for (int j = 1; j<=N; j++) cin >> X[i][j];
    }
    int dp[N+1][int(pow(2,K))];
    for (int i = 0; i<N+1; i++){
        for (int j = 0; j<pow(2,K); j++){
            dp[i][j] = mx;
        }
    }
    dp[0][0] = 0;
    for (int i = 0; i<N; i++){
        for (int j = 0; j<pow(2,K); j++){
            if (dp[i][j]==mx) continue;
            int res = 0;
            for (int k = 0; k<K; k++) res^=X[k][i+1];
            for (int k = 0; k<K; k++){
                if (!((j>>k)&1))
                    dp[i+1][j|(1<<k)] = min(dp[i+1][j|(1<<k)], dp[i][j]+(res^X[k][i+1]));
            }
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+res);
        }
    }
    int ans = mx;
    for (int i = 0; i<pow(2,K); i++) ans = min(ans, dp[N][i]);
    cout << ans;
}