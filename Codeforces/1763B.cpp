#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
bool comp(const pii &a, const pii &b){
    return a.second < b.second;
}

main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        int n, k;
        cin >> n >> k;
        int h[n];
        int p[n];
        for (int i = 0; i<n; i++){
            cin >> h[i];
        }
        for (int i = 0; i<n; i++){
            cin >> p[i];
        }
        multiset<pii> fr; // sort by health
        multiset<pii> sd; // sort by power
        for (int i = 0; i<n; i++){
            fr.insert(mp(h[i], p[i]));
            sd.insert(mp(p[i], h[i]));
        }
        int s = 0;
        while (k > 0){
            s += k;
            pii smol = *fr.begin();
            while (s >= smol.first){
                fr.erase(fr.begin());
                sd.erase(sd.find(mp(smol.second, smol.first)));
                if (!fr.size()) break;
                smol = *fr.begin();
            }
            if (!fr.size()) break;
            pii smal = *sd.begin();
            k -= smal.first;
            if (k <= 0) break;
        }
        if (fr.size()) cout << "NO\n";
        else cout << "YES\n";
    }
}
