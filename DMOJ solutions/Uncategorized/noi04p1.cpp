#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
tree<
pii,
null_type,
greater<pii>,
rb_tree_tag,
tree_order_statistics_node_update>
ost;
map<int,int>cnt;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, slave, tot, base, k, l;
    char t;
    cin >> N >> slave;
    l = 0;
    base = 0;
    for (int i = 0; i<N; i++){
        cin >> t >> k;
        if (t == 'I'){
            if (k<slave){
                continue;
            }
            k -= base;
            if (cnt.count(k))cnt[k]++;
            else cnt[k] = 1;
            ost.insert(mp(k, cnt[k]));
        }
        else if (t == 'A'){
            base += k;
        }
        else if (t == 'S'){
            base -=k;
            while (ost.size()&&(*ost.find_by_order(ost.size()-1)).first+base < slave){
                int p = (*ost.find_by_order(ost.size()-1)).first;
                ost.erase(mp(p, cnt[p]));
                cnt[p]--;
                if(!cnt[p]){cnt.erase(p);}
                l++;
            }
        }
        else{
            int res = -1;
            if (k <= ost.size()) res = (*ost.find_by_order(k-1)).first+base;
            cout << res << "\n";
        }
    }
    cout << l << "\n";
}