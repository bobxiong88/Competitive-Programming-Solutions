#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define mx int(5e5)+5
int k;
struct q{
    int l, r, i;
};
int get(int x){
    return x/k;
}
bool comp(const q &x, const q &y){
    return x.r<y.r;
}
int a[mx], ans[mx], freq[mx];
vector<q> queries[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, l, r;
    cin >> N >> Q;
    k = sqrt(N)+1;
    set<int> str;
    for (int i = 1; i<=N; i++){
        cin >> a[i];
        str.insert(a[i]);
    }
    vector<int> v(str.begin(), str.end());
    sort(v.begin(), v.end());
    map<int,int> mp;
    for (int i = 0; i<v.size(); i++){
        mp[v[i]] = i;
    }
    for (int i = 1; i<=N; i++){
        a[i] = mp[a[i]];
    }
    for (int i = 0; i<Q; i++){
        cin >> l >> r;
        queries[get(l)].pb({l, r, i});
    }
    for (int i = 0; i<k+1; i++){
        sort(queries[i].begin(), queries[i].end(), comp);
    }
    for (int x = 0; x<k+1; x++){
        vector<q> blk = queries[x];
        if (blk.size() == 0) continue;
        auto [l, r, i] = blk[0];
        int res = 0;
        for (int j = l; j <= r; j++){
            freq[a[j]]++;
            if (freq[a[j]] == 2) res++;
            else if (freq[a[j]] == 3) res--;
        }
        ans[i] = res;
        int cnt = 0;
        int ll = l;
        int lr = r;
        for (auto[l, r, i]: blk){
            if (!cnt){
                cnt++;
                continue;
            }
            if (ll > l){
                for (int j = l; j<ll; j++){
                    freq[a[j]]++;
                    if (freq[a[j]] == 2) res++;
                    else if (freq[a[j]] == 3) res--;
                }
            }
            else{
                for (int j = ll; j<l; j++){
                    freq[a[j]]--;
                    if (freq[a[j]] == 2) res++;
                    else if (freq[a[j]] == 1) res--;
                }
            }
            for (int j = lr+1; j<=r; j++){
                freq[a[j]]++;
                if (freq[a[j]] == 2) res++;
                else if (freq[a[j]] == 3) res--;
            }

            ll = l;
            lr = r;
            ans[i] = res;
        }
        memset(freq, 0, N+1);
    }
    for (int i = 0; i<Q; i++){
        cout << ans[i] << "\n";
    }
}