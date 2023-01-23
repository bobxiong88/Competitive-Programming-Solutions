#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mx 105
int dist[mx][mx][mx];
int ans[mx][mx][mx];
struct lol{
    int x, y, z, i;
};
struct poo{
    int i, j, k;
};
int main(){
    for (int i = 0; i<mx; i++){
        for (int j = 0; j<mx; j++){
            for (int k = 0; k<mx; k++){
                dist[i][j][k] = int(1e9);
                ans[i][j][k] = int(1e9);
            }
        }
    }
    ios_base::sync_with_stdio(false); cin.tie(0);
    int n, q, x, y, z, idx;
    cin >> n >> q;
    queue<lol> que;

    for (int i = 1; i<=n; i++){
        cin >> x >> y >> z;
        que.push({x, y, z, i});
        dist[x][y][z] = 0;
        ans[x][y][z] = i;
    }
    while (!que.empty()){
        lol obj = que.front(); que.pop();
        int d = dist[obj.x][obj.y][obj.z];
        vector<poo> gay= {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}, {-1, 0, 0}, {0, -1, 0}, {0, 0, -1}};
        for (auto[i,j,k]:gay){
            int a = i+obj.x;
            int b = j+obj.y;
            int c = k+obj.z;
            if (0 <= a && a <mx && 0 <= b && b < mx && 0 <= c && c < mx){
                if (dist[a][b][c] > d+1 || (dist[a][b][c] == d+1 && ans[a][b][c] > obj.i)){
                    que.push({a, b, c, obj.i});
                    dist[a][b][c] = d+1;
                    ans[a][b][c] = obj.i;
                }
            }
        }
    }
    while (q--){
        cin >> x >> y >> z;
        cout << ans[x][y][z] << "\n";
    }
    return 0;
}