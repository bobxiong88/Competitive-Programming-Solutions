#include <bits/stdc++.h>
using namespace std;
#define mx 200005
#define nx 25
int player[mx][nx];
int M, N, K, diff, v, ans;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> M >> N >> K;
    for (int i = 0; i<M; i++){
        for (int j = 0; j<N; j++){
            cin >> player[i][j];
        }
    }
    ans = 0;
    for (int t = 0; t<N-1; t++){
        unordered_map<int, int> val;
        for (int x = 0; x<M; x++){
            diff = player[x][t+1]-player[x][t];
            v = player[x][t]+diff-K;
            if (val.count(v) && val[v] == diff){
                ans += 1;
            }
            val[player[x][t+1]] = diff;
        }
    }
    for (int t = 0; t<N-1; t++){
        unordered_map<int, int> val;
        for (int x = M-1; x>=0; x--){
            diff = player[x][t+1]-player[x][t];
            v = player[x][t]+diff-K;

            if (val.count(v) && val[v] == diff){
                ans += 1;
            }
            val[player[x][t+1]] = diff;
        }
    }
    cout << ans << "\n";
}