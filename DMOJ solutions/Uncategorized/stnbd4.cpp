#include <bits/stdc++.h>
using namespace std;
using blm = long long;
//#define int blm
#define mx int(5e5)+5
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
int a[mx], bit[mx];
blm ans[mx];
int k;
struct q{
    int l, r, i;
};
bool comp(const q &x, const q &y){
    return x.r < y.r;
}
int lsb(int x){
    return x&(-x);
}
int query(int x){
    blm res = 0;
    for (int i = x; i>0; i-=lsb(i)) res += bit[i];
    return res;
}
void update(int x, int v){
    for (int i = x; i<mx; i+=lsb(i)) bit[i] += v;
}
int qa(int l, int r){
    return query(r)-query(l-1);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, l, r;
    cin >> N;
    set<int> str;
    for (int i = 1; i<=N; i++){
        cin >> a[i];
        str.insert(a[i]);
    }
    k = sqrt(N)+1;
    vector<q> sex[k+1];
    vector<int> v(str.begin(), str.end());
    sort(v.begin(), v.end());
    map<int,int> mp;
    for (int i = 0; i<v.size(); i++){
        mp[v[i]] = i+1;
    }

    for (int i = 1; i<=N; i++){
        a[i] = mp[a[i]];
    }
    cin >> Q;
    for (int i = 0; i<Q; i++){
        cin >> l >> r;
        sex[l/k].pb({l, r, i});
    }
    int cnt = 0;
    for (auto blk: sex){
        if (blk.size() == 0) continue;
        sort(blk.begin(), blk.end(), comp);
        int ll = blk[0].l;
        int lr = blk[0].l-1;
        blm res = 0;
        //cout << "for block " << cnt++ << "\n";
        for (auto[l, r, i] : blk){
            for (int j = lr+1; j <= r; j++){
                update(a[j], 1);
                res += qa(a[j]+1, N+1);
            }
            if (ll > l){
                for (int j = ll-1; j >= l; j--){
                    update(a[j], 1);
                    res += qa(1, a[j]-1);
                }
            }
            else{
                for (int j = ll; j<l; j++){
                    update(a[j], -1);
                    res -= qa(1, a[j]-1);
                }
            }
            ll = l;
            lr = r;
            ans[i] = res;
            //cout << l << " " << r << " " << res << "\n";
        }
        memset(bit, 0, mx);
    }
    for (int i = 0; i<Q; i++) cout << ans[i] << "\n";
}