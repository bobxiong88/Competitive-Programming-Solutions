#include <bits/stdc++.h>
using namespace std;
#define mx 10005
#define pb push_back
vector<int> crd[mx];
int cnt[mx];
int N, M, x, y, w, h, ans, curr;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> M;
    while (M--){
        cin >> x >> y >> w >> h;
        crd[x].pb(y); crd[x].pb(y+h);
        crd[x+w].pb(y); crd[x+w].pb(y+h);
    }
    ans = 0;
    for (int i = 0; i<=N+1; i++){
        for (int k : crd[i])
            cnt[k] ^= 1;
        curr = 0;
        for (int j = 0; j<=N+1; j++){
            curr ^= cnt[j];
            ans += curr;
        }
    }
    cout << ans;
}