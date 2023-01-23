#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define m 3001
#define n 3001
int N, K;
int LSB(int x){
    return x & (-x);
}
int gay[3000][3000];
int grid[m][n];
int bit[m][n];
int query(int x, int y){
    int mx = 0;
    for (int xi = x; xi > 0; xi -= LSB(xi)){
        for (int yi = y; yi > 0; yi -= LSB(yi)){
            mx = max(mx,bit[xi][yi]);
        }
    }
    return mx;
}
void update(int x, int y, int value){
    for (int xi = x; xi < m; xi += LSB(xi)){
        for (int yi = y; yi < n; yi += LSB(yi)){
            bit[xi][yi] = max(bit[xi][yi],value);
        }
    }
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    cin >> N >> K;
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            if (j > N-i) cin >> grid[i][j];
        }
    }
    int ans = 0;
    for (int i = 1; i <= N; i++){
        for (int j = N-i+1; j <= N; j++)
            update(j, N*2-i-j+1, grid[j][N*2-i-j+1]);
        if (i >= K){
            for (int j = N-i+K; j <= N; j++)
                ans += query(j, N*2-i-j+K);
        }
    }
    cout << ans;
}