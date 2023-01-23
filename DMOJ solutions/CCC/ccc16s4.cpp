#include <bits/stdc++.h>
using namespace std;
#define mx 405
int N, ans;
int sz[mx][mx], a[mx];
bool pos[mx][mx], vis[mx][mx];
bool check(int l, int r){
    if (vis[l][r]) return pos[l][r];
    vis[l][r] = true;
    for (int i = l; i < r; i++){
        if (sz[l][i] == sz[i+1][r]){
            if (check(l, i) && check(i+1, r)){
                pos[l][r] = true;
                return true;
            }
        }
        else if(sz[l][i] > sz[i+1][r])
            break;
    }
    for (int i = l; i<r-1; i++){
        if (check(l, i)){
            if (sz[l][i] < sz[i+1][r]){
                for (int j = i+1; j < r; j++){
                    if (sz[l][i] == sz[j+1][r]){
                        if (check(i+1, j) && check(j+1, r)){
                            pos[l][r] = true;
                            return true;
                        }
                    }
                    else if (sz[l][i] > sz[j+1][r])
                        break;
                }
            }
            else
                break;
        }
    }
    return false;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin >> N;
    for (int i = 0; i<N; i++) cin >> a[i];
    for (int i = 0; i<N; i++){
        pos[i][i] = true;
        vis[i][i] = true;
        for (int j = i; j<N; j++){
            if (j) sz[i][j] = sz[i][j-1]+a[j];
            else sz[i][j] = a[j];
        }
    }
    for (int i = 0; i<N; i++){
        for (int j = i; j<N; j++){
            if (sz[i][j] > ans && check(i, j)) ans = sz[i][j];
        }
    }
    cout << ans;
}