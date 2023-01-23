#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
int N, M, res, m, a, b;
int tb[500005];
string S;
set<int> bit;
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    m = 1e9+7;
    cin >> N >> M;
    cin >> S;
    tb[0] = 1;
    for (int i = 1; i<500005; i++)
        tb[i] = (tb[i-1]*2)%m;
    for (int i = 0; i<N; i++){
        if (S[i] == '0') bit.insert(i);
        else res += tb[N-i-1];
    }
    while (M--){
        cin >> a >> b;
        a--; b--;
        for (auto it = bit.lower_bound(a); *it <= b && it != bit.end(); it = bit.lower_bound(*it)){
            res = (res + tb[N-*it-1])%m;
            bit.erase(*it);
        }
        cout << res << "\n";
    }
}