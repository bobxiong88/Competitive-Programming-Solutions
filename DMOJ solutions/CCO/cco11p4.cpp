#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
tree<
pii,
null_type,
less<pii>,
rb_tree_tag,
tree_order_statistics_node_update> ost;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int n, R, k;
    cin >> n;
    cin >> R;
    ost.insert(mp(R, 1)); ost.insert(mp(R, 2));
    for (int i = 1; i<n; i++){
        cin >> R;
        k = ost.order_of_key(mp(R, 1))-1;
        pii p = *ost.find_by_order(k);
        //cout << p.first << " " << p.second << " " << R << " " << k << "\n";
        if (p.first < R && k != -1){
            ost.erase(p);
            ost.insert(mp(R, 1));
            ost.insert(mp(R, 2));
        }
        else{
            cout << "NO\n";
            return 0;
        }
    }
    cout << "YES\n";
}