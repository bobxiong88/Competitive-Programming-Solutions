#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
struct item{
    int m, v;
};
int n, k, m, v, c;
int t[600005][2];
void build(){
    for (int i = n-1; i>0; --i){
        if (t[i<<1][0] >= t[i<<1|1][0]){
            t[i][0] = t[i<<1][0];
            t[i][1] = t[i<<1][1];
        }
        else{
            t[i][0] = t[i<<1|1][0];
            t[i][1] = t[i<<1|1][1];
        }
    }
}
void update(int p, int value){
    for (t[p += n][0] = value; p > 1; p >>= 1){
        if (t[p][0] >= t[p^1][0]){
            t[p>>1][0] = t[p][0];
            t[p>>1][1] = t[p][1];
        }
        else{
            t[p>>1][0] = t[p^1][0];
            t[p>>1][1] = t[p^1][1];
        }
    }
}
int query(int l, int r){
    r++;
    int mx = -1;
    int idx = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1){
            l++;
            if (t[l-1][0]>mx){
                mx = t[l-1][0];
                idx = t[l-1][1];
            }
        }
        if (r&1){
            --r;
            if (t[r][0]>mx){
                mx = t[r][0];
                idx = t[r][1];
            }
        }
    }
    update(idx, 0);
    return mx;
}
vector <int> bag;
vector <item> arr;
bool pog(const item &a, const item &b)
{
    return a.m < b.m;
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> k;
    n++;
    arr.push_back(item{0,0});
    bag.push_back(0);
    for (int i = 1; i < n; i++){
        cin >> m >> v;
        arr.push_back(item({m,v}));
    }
    for (int i = 0; i<k; i++){
        cin >> c;
        bag.push_back(c);
    }
    sort(arr.begin(), arr.end(), pog);
    sort(bag.begin(), bag.end());
    for (int i = 1; i < n; ++i){
        t[i+n][0] = arr[i].v;
        t[i+n][1] = i;
    }
    build();
    int ans = 0;
    int curr = 1;
    for (int i = 1; i <= k; i++){
        while (arr[curr].m <= bag[i]){
            curr++;
            if (curr >= arr.size()) break;
        }
        curr--;
        ans += query(1, curr);
    }
    cout << ans << "\n";
}