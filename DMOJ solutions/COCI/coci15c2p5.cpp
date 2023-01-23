#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define mx int(2e6)+5
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
int bit[mx];
ll psa[mx];
vector<ll> deez;
int lsb(int x){
    return x&(-x);
}
int qry(int x){
    int res = 0;
    for (int i = x; i>0; i-=lsb(i)) res += bit[i];
    return res;
}
void upd(int x, int v){
    for (int i = x; i<mx; i+=lsb(i)) bit[i] += v;
}
int get(ll x){
    int l = 0;
    int r = deez.size()-1;
    while (l <= r){
        int m = (l+r)/2;
        if (deez[m] == x) return m;
        if (deez[m] > x){
            r = m-1;
        }
        else {
            l = m+1;
        }
    }
}
int main(){
     ios_base::sync_with_stdio(false); cin.tie(0);
    int N, P;
    cin >> N;
    for (int i = 1; i<=N; i++) cin >> psa[i];
    cin >> P;
    for (int i = 1; i<=N; i++) {
        psa[i] += psa[i-1]-P;
        deez.pb(psa[i]);
    }
    deez.pb(0);
    sort(deez.begin(), deez.end());
    int j = 0;
    for (int i = 0; i<deez.size(); i++){
        if (i==0||deez[i]!=deez[i-1]){
            deez[j] = deez[i];
            j++;
        }
    }
    upd(get(0)+1, 1);
    ll ans = 0;
    for (int i = 1; i<=N; i++){
        int x = get(psa[i])+1;
        ans += qry(x);
        upd(x, 1);
    }
    cout << ans << "\n";
}