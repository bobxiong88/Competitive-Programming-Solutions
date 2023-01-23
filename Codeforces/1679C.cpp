#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
const int mx = int(2e5)+5;
int sx[mx], sy[mx];
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    int n, q;
    cin >> n >> q;
    set<int> ex, ey;
    for (int i = 1; i<=n+1; i++){
        ex.insert(i);
        ey.insert(i);
    }
    while (q--){
        int t, x, y, x1, x2, y1, y2;
        cin >> t;
        if (t == 1){
            cin >> x >> y;
            sx[x]++; sy[y]++;
            if (sx[x] == 1) ex.erase(x);
            if (sy[y] == 1) ey.erase(y);
        }
        else if (t == 2){
            cin >> x >> y;
            sx[x]--; sy[y]--;
            if (sx[x] == 0) ex.insert(x);
            if (sy[y] == 0) ey.insert(y);
        }
        else{
            cin >> x1 >> y1 >> x2 >> y2;
            //cout << *ex.lower_bound(x1) << " " << *ey.lower_bound(y1) << "\n";
            int a = *ex.lower_bound(x1) > x2;
            int b = *ey.lower_bound(y1) > y2;
            if (a||b) cout << "Yes\n";
            else cout << "No\n";
        }
    }
}
