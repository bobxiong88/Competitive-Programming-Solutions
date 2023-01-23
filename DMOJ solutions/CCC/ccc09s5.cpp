#include <bits/stdc++.h>
using namespace std;
#define xm 1005
#define ym 30005
int N, M, R, K, B, x, y;
int diff[xm][ym];
int a[xm][ym];
void update(int i, int l, int r, int x){
    diff[i][l] += x;
    diff[i][r+1] -= x;
}
void get(){
    for (int i = 1; i<=N; i++){
        for (int j = 1; j<=M; j++)
            a[i][j] = diff[i][j]+a[i][j-1];
    }
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    for (int i = 0; i<xm; i++){
        for (int j = 0; j<ym; j++){
            a[i][j] = 0;
            diff[i][j] = 0;
        }
    }
    cin >> M;
    cin >> N;
    cin >> K;
    while (K--){
        cin >> x >> y >> R >> B;
        for (int i = 0; x+i <= min(x+R, N); i++){
            int d = sqrt(pow(R, 2)-pow(i,2));
            int l = max(1, y-d);
            int r = min(M, y+d);
            update(x+i, l, r, B);
        }
        for (int i = 1; x-i >= max(1, x-R); i++){
            int d = sqrt(pow(R, 2)-pow(i,2));
            int l = max(1, y-d);
            int r = min(M, y+d);
            update(x-i, l, r, B);
        }
    }
    get();
    int ans = 0;
    int mx = 0;
    for (int i = 1; i<=N; i++){
        for (int j = 1; j<=M; j++){
            if (a[i][j] > mx){
                mx = a[i][j];
                ans = 1;
            }
            else if (a[i][j] == mx){
                ans++;
            }
        }
    }
    cout << mx << "\n" << ans << "\n";
}