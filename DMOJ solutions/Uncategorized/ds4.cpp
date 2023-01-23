#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
tree<
pii,
null_type,
less<pii>,
rb_tree_tag,
tree_order_statistics_node_update>
ost;
int N, M, v, res;
char t;
map<int, int> cnt;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N >> M;
    for (int i = 0; i<N; i++){
        cin >> v;
        if (cnt.count(v)) cnt[v]++;
        else cnt[v] = 1;
        ost.insert(mp(v, cnt[v]));
    }
    res = 0;
    while (M--){
        cin >> t >> v;
        v ^= res;
        if (t == 'I'){
            if (cnt.count(v)) cnt[v]++;
            else cnt[v] = 1;
            ost.insert(mp(v, cnt[v]));
        }
        else if (t == 'R'){
            if (cnt.count(v)){
                ost.erase(mp(v, cnt[v]));
                cnt[v]--;
                if (cnt[v] == 0) cnt.erase(v);
            }
        }
        else if (t == 'S'){
            auto k = *ost.find_by_order(v-1);
            res = k.first;
            cout << res << "\n";
        }
        else{
            if (!cnt.count(v)) res = -1;
            else res = ost.order_of_key(mp(v, 1))+1;
            cout << res << "\n";
        }
    }
    vector<int> burger;
    for (auto [key, value]: cnt){
        while (value--){
            burger.pb(key);
        }
    }
    for (int k: burger){
        cout << k << " ";
    }
}