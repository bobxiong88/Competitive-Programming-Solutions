#include <bits/stdc++.h>
using namespace std;
const int mx = 21;
double dp[int(pow(2, mx))];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N;
    cin >> N;
    double v[N][N];
    for (int i = 0; i<N; i++){
        for (int j = 0; j<N; j++)
            cin >> v[i][j];
    }
    dp[0] = 1;
    for (int j = 0; j<int(pow(2,N)); j++){
        int i = 0;
        for (int k = 0; k<N; k++)
            i += (j>>k)&1;
        for (int k = 0; k<N; k++){
            if (!((j >> k)&1))
                dp[j|(1<<k)] = max(dp[j|(1<<k)], dp[j]*v[i][k]/100);
        }

    }
    cout << fixed << setprecision(10);
    cout << dp[int(pow(2, N))-1]*100;
}