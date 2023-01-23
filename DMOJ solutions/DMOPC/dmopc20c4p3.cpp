#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define mp make_pair
#define pb push_back
#define mx 1000005
vector<pair<int,int>> cord;
vector<pair<int,int>> room;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update> seen;
int N, M, x, y;
int bit[mx];
int LSB(int x){
    return x&(-x);
}
int query(int x){
    int res = 0;
    for (int i = x; i>0; i-=LSB(i))
        res += bit[i];
    return res;
}
void update(int x, int v){
    for (int i = x; i<mx; i+=LSB(i))
        bit[i] += v;
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> M;
    vector<int> piss;
    map<int,int> okay;
    for (int i = 0; i<N; i++){
        cin >> x >> y;
        piss.pb(y);
        room.pb(mp(x, y));
    }
    for (int i = 0; i<M; i++){
        cin >> x >> y;
        piss.pb(y);
        cord.pb(mp(x, y));
    }
    x = 0;
    sort(piss.begin(), piss.end());
    for (int i = 0; i<piss.size();i++){
        if (i){
            if (piss[i-1]!=piss[i]){
                okay[piss[i]] = ++x;
            }
        }
        else{
            okay[piss[i]] = ++x;
        }
    }
    sort(cord.begin(), cord.end(),greater<pair<int,int>>());
    sort(room.begin(), room.end());
    ll ans = 0;
    for (auto [a,b]:cord){
        while (!room.empty() && (room.back().first >= a)){
            int temp = room.back().second;
            update(okay[temp], 1);
            room.pop_back();
        }
        ans += query(okay[b]);
    }
    cout << ans << "\n";
    return 0;
}
