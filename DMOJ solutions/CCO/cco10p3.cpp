#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define mp make_pair
#define pii pair<int,int>
tree<pii, null_type,greater<pii>, rb_tree_tag,tree_order_statistics_node_update> fart;
vector<int> rate(1000005);
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, X, R, K;
    pii temp;
    char t;
    cin >> N;
    while (N--){
        cin >> t;
        if (t == 'N'){
            cin >> X >> R;
            fart.insert(mp(R, X));
            rate[X] = R;
        }
        else if (t == 'M'){
            cin >> X >> R;
            fart.erase(mp(rate[X], X));
            fart.insert(mp(R, X));
            rate[X] = R;
        }
        else{
            cin >> K;
            temp = *fart.find_by_order(K-1);
            cout << temp.second << "\n";
        }
    }
}