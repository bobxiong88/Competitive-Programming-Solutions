#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
vector<pii> pnt;
int N, M, r, c, mc, lr, lc, k, d, ans;
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> M;
    for (int i = 0; i<M; i++){
        cin >> r >> c;
        pnt.pb(mp(c, r));
        mc = max(mc, c+N-r+1);
    }
    pnt.pb(mp(mc, N));
    sort(pnt.begin(), pnt.end());
    lc = pnt[0].first;
    lr = pnt[0].second;
    for (auto[c, r]: pnt){
        // inside
        if (c-lc <= r-lr){
        }
        // outside
        else if (c-lc > N-lr){
            k = N-lr+1;
            ans += k*(k+1)/2;
            lr = r;
            lc = c;
        }
        // shared
        else{
            k = N-lr+1;
            d = c-lc;
            ans += k*(k+1)/2-(k-d)*(k-d+1)/2;
            lr = r; lc = c;
        }
    }
    cout << ans << "\n";
}