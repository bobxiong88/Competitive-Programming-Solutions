#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pii pair<int,int>
#define mx int(1e5)+5
const int sz = 1000;
bitset<sz> gay;
bitset<sz> t[2*mx];
map<int,int> cnt, pos;
vector<int> sex;
void update(int p, int x){
    for (t[p += mx].flip(x); p > 1; p>>=1){
        t[p >> 1] = t[p]|t[p^1];
    }
}
int query(int l, int r){
    r++;
    bitset<sz> res;
    res.reset();
    for (l += mx, r += mx; l < r; l >>= 1, r >>= 1){
        if (l&1) res = res| t[l++];
        if (r&1) res = res| t[--r];
    }
    return res.count();
}
int a[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, T, x, y;
    for (int i = 0; i<1000; i++){
        sex.pb(i);
    }
    cin >> N >> Q;
    for (int i = 1; i<=N; i++){
        cin >> a[i];
        if (!cnt[a[i]]){
            pos[a[i]] = sex.back();
        sex.pop_back();
        }
        cnt[a[i]]++;
        update(i, pos[a[i]]);
    }
    while(Q--){
        cin >> T >> x >> y;
        if (T == 1){
            cnt[a[x]]--;
            update(x, pos[a[x]]);
            if (!cnt[a[x]]){
                sex.pb(pos[a[x]]);
                cnt.erase(a[x]);
                pos.erase(a[x]);
            }
            cnt[y]++;
            if (!pos.count(y)){
                pos[y] = sex.back(); sex.pop_back();
            }
            update(x, pos[y]);
            a[x] = y;
        }
        else{
            cout << query(x, y) << "\n";
        }
    }
}