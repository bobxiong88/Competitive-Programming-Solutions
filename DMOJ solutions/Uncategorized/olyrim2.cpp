//modified Al.Cash's iterative segment tree template
#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
using ll = long long;
//OR - let a be the number of 1s in a bit, sum = E (0, 27)(ai(n-ai)+ai(ai-1)/2)*2^i
//AND - sum = E (0, 27) (ai(ai-1)/2)*2^i
//XOR - sum = E (0, 27) (ai*(n-ai))*2^i
int t[200005][32];
int n, Q, a, b, q;
void build(){
    for (int i = n - 1; i > 0; --i){
        for (int x = 0; x<32; x++) t[i][x] = t[i<<1][x] + t[i<<1|1][x];
    }
}
void update(int p, int value){
    p+=n;
    bitset<32> b(value);
    for (int x = 0; x<32; x++) t[p][x] = b.test(x);
    for (; p > 1; p >>= 1) {
        for (int x = 0; x<32; x++) t[p>>1][x] = t[p][x] + t[p^1][x];
    }
}
ll p(int x, int v){
    ll a = 1;
    for (int i = 0; i<v; i++){
        a*=x;
    }
    return a;
}
ll query(int l, int r, int type){
    r++;
    ll num = r-l;
    int res[32] = {0};
    //for(auto i:res) cout << i;
    //cout << "\n";
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1){
            l++;
            for (int x = 0; x<32; x++) res[x] += t[l-1][x];
        }
        if (r&1){
            --r;
            for (int x = 0; x<32; x++) res[x] += t[r][x];
        }
    }
    ll ans = 0;
    ll a;
    for (int i = 0; i<32; i++){
        a = res[i];
        switch (type){
            case 2:
                ans += (a*(num-a)+a*(a-1)/2)*p(2,i);
                break;
            case 3:
                ans += (a*(a-1)/2)*p(2,i);
                break;
            case 4:
                ans += (a*(num-a))*p(2,i);
                break;
        }
    }
    return ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> Q;
    n++;
    for (int i = 1; i<n; ++i){
        cin >> a;
        bitset<32> b(a);
        for(int x = 0; x<32; x++) t[n+i][x] = b.test(x);
    }
    build();
    for (int i = 0; i<Q; i++){
        cin >> q >> a >> b;
        if (q == 1) update(a,b);
        else cout << query(a, b, q) << "\n";
    }

}