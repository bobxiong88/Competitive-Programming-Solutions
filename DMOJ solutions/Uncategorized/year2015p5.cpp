#include <bits/stdc++.h>
using namespace std;
using ll = __int128;
ll get(char c){
    return int(c)-96;
}
vector<bitset<2001>> adj(2001);
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    set<ll> a;
    string S, W;
    int N, n, ans;
    ll v, p, m;
    p = 31; m = 100123456789;
    cin >> S;
    n = S.length();
    cin >> N;
    while (N--){
        cin >> W;
        v = 0;
        for (int i = 0; i<W.length(); i++) v = (v*p+get(W[i]))%m;
        a.insert(v);
    }
    for (int i = n-1; i>=0; i--){
        v = 0;
        for (int j = i; j<n; j++){
            v  = (v*p+get(S[j]))%m;
            if (a.count(v)){
                adj[i] |= adj[j+1];
                adj[i][j+1] = 1;
            }
        }
    }
    ans = 0;
    for (int i = 0; i<n+1; i++){
        ans += adj[i].count();
    }
    cout << ans;
}