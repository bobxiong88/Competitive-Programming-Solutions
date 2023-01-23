#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int N, M, x, y, sm, pm, sv, pv;
    cin >> N >> M;
    int mx = 500000;
    int inf = 2000000000;
    vector<vector<int>> arr;
    for (int t = 0; t<N; t++){
        cin >> x >> y >> sm >> pm >> sv >> pv;
        int dp[mx+1];
        for(int i = 0; i<mx+1; i++) dp[i] = inf;
        dp[y] = 0;
        int ok[2][2] = {{sm, pm},{sv, pv}};
        for(auto pr: ok){
            int s = pr[0];
            int p = pr[1];
            for (int i = 1; i<mx+1; i++){
                if (s <= i){
                    int res = dp[i-s];
                    if(res != inf && res+p < dp[i])
                        dp[i] = res + p;
                }
            }
        }
        vector<int> costs;
        int m = inf;
        for(int i = mx; i>= x; i--){
            m = min(m, dp[i]);
            if (i%x == 0)
                costs.push_back(m);
        }
        reverse(costs.begin(), costs.end());
        arr.push_back(costs);
    }
    int ans = 0;
    for(int i = 0; i<mx; i++){
        int s = 0;
        for (int x = 0; x<N; x++){
            if (i == arr[x].size()){
                cout << i-1;
                return 0;
            }
            s += arr[x][i];
        }
        ans = i;
        if (s > M)
            break;
    }
    cout << ans;
}