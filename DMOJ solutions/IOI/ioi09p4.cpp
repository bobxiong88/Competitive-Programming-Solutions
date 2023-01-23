#include <bits/stdc++.h>
using namespace std;
#define mx 55
int dp[mx][mx][mx][mx];
int psa[mx][mx];
bool used[mx][mx][mx][mx];
int a[mx][mx];
int sum(int x1, int y1, int x2, int y2){
    return psa[x2][y2]-psa[x2][y1-1]-psa[x1-1][y2]+psa[x1-1][y1-1];
}
int get(int x1, int y1, int x2, int y2){
    if (used[x1][y1][x2][y2]) return dp[x1][y1][x2][y2];
    if (x1 == x2 && y1 == y2) return 0;
    int val = int(1e9);
    for (int x = x1; x < x2; x++){
        val = min(val, get(x1, y1, x, y2)+get(x+1, y1, x2, y2));
    }
    for (int y = y1; y < y2; y++){
        val = min(val, get(x1, y1, x2, y)+get(x1, y+1, x2, y2));
    }
    val += sum(x1, y1, x2, y2);
    used[x1][y1][x2][y2] = true;
    dp[x1][y1][x2][y2] = val;
    return val;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M, x;
    cin >> N >> M;
    for (int i = 1; i<=N; i++){
        for (int j = 1; j<=M; j++){
            cin >> x;
            psa[i][j] = psa[i-1][j]+psa[i][j-1]-psa[i-1][j-1]+x;
        }
    }
    cout << get(1, 1, N, M) << "\n";
}