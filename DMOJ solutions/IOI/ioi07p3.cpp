#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
const int mx = int(1e5)+5;
int t[4*mx], lazy[4*mx];
int maxh;
void lazyUpdate(int node, int tl, int tr){
    if (lazy[node]!=0){
        t[node] += (tr-tl+1)*lazy[node];
        if (tl != tr){
            lazy[node*2] += lazy[node];
            lazy[node*2+1]+=lazy[node];
        }
        lazy[node] = 0;
    }
}
void update(int node, int tl, int tr, int l, int r){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr) return;
    if (l <= tl && tr <= r){
        t[node] += tr-tl+1;
        if (tl != tr){
            lazy[node*2]++;
            lazy[node*2+1]++;
        }
        return;
    }
    int tm = (tl+tr)/2;
    update(node*2, tl, tm, l, r);
    update(node*2+1, tm+1, tr, l, r);
    t[node] = t[node*2]+t[node*2+1];
}
int query(int node, int tl, int tr, int x){
    if (x < tl || x > tr) return 0;
    lazyUpdate(node, tl, tr);
    if (tl == tr && tl == x) return t[node];
    int tm = (tl+tr)/2;
    return query(node*2, tl, tm, x)+query(node*2+1, tm+1, tr, x);
}
int get(int x){
    return query(1, 1, maxh, x);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N;
    cin >> N;
    maxh = 0;
    vector<pii> sails;
    for (int i = 0; i<N; i++){
        int h,k;
        cin >> h >> k;
        maxh = max(maxh, h);
        sails.pb(mp(h, k));
    }
    sort(sails.begin(), sails.end());
    for (auto [h,k]: sails){
        int l = h-k+1;
        int r = h;
        int val = get(l);
        while (l < r){
            int m = (l+r)/2+(l+r)%2;
            if (get(m) != val){
                r = m-1;
            }
            else{
                l = m;
            }
        }
        int idx = l;
        l = 1;
        r = idx;
        while (l < r){
            int m = (l+r)/2;
            if (get(m) != val){
                l = m+1;
            }
            else{
                r = m;
            }
        }
        update(1, 1, maxh, idx+1, h);
        k -= h-idx;
        update(1, 1, maxh, l, l+k-1);
        //for (int i = 0; i<=maxh; i++) cout << get(i) << " "; cout << "\n";
    }
    long long ans = 0;
    for (int i = 1; i<=maxh; i++){
        long long v = get(i);
        ans += v*(v-1);
    }
    cout << ans/2 << "\n";
}
/*
6
2 1
3 2
3 2
4 1
4 3
5 3
*/