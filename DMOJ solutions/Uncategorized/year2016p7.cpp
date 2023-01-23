#include <bits/stdc++.h>
using namespace std;
#define mx int(1e5)+5
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define inf int(2e9)
int tmax[2*mx];
int tmin[2*mx];
pii tres[2*mx];
int a[mx];
int res[mx];
int n, K;
pii get(pii a, pii b){
    if (a.first < b.first) return a;
    if (a.first > b.first) return b;
    if (a.second < b.second) return a;
    return b;
}
void bmax(){for (int i = n-1; i>0; i--) tmax[i] = max(tmax[i<<1], tmax[i<<1|1]);}
void bmin(){for (int i = n-1; i>0; i--) tmin[i] = min(tmin[i<<1], tmin[i<<1|1]);}
void bres(){for (int i = n-1; i>0; i--) tres[i] = get(tres[i<<1], tres[i<<1|1]);}
int qmax(int l, int r){
    r++;
    int res = -inf;
    for (l += n, r += n; l < r; l>>=1, r>>=1){
        if (l&1) res = max(res, tmax[l++]);
        if (r&1) res = max(res, tmax[--r]);
    }
    return res;
}
int qmin(int l, int r){
    r++;
    int res = inf;
    for (l += n, r += n; l < r; l>>=1, r>>=1){
        if (l&1) res = min(res, tmin[l++]);
        if (r&1) res = min(res, tmin[--r]);
    }
    return res;
}
pii qres(int l, int r){
    r++;
    pii res = mp(inf, inf);
    for (l += n, r += n; l < r; l>>=1, r>>=1){
        if (l&1) res = get(tres[l++], res);
        if (r&1) res = get(tres[--r], res);
    }
    return res;
}
int range(int l, int r){
    return qmax(l, r) - qmin(l, r);
}
int bs(int l, int r){
    int i = l;
    if (range(l, r) <= K) return r-l+1;
    while (l <= r){
        int m = (l+r)/2;
        int a = range(i, m);
        int b = range(i, min(m+1, n-1));
        if (a <= K && b > K) return m-i+1;
        if (a > K) r = m-1;
        else l = m+1;
    }
}
int bs2(int l, int r){
    if (res[r] == 1) return r;
    int ll = l;
    int rr = r;
    while (l <= r){
        int m = int(l+r)/2;
        int a = res[m]+m-1;
        int b = res[m+1]+m+1-1;
        if (a <= rr && b > rr) return m;
        if (a > rr) r = m-1;
        else l = m+1;
    }
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int Q;
    cin >> n >> K;
    for (int i = 0; i<n; i++){
        cin >> a[i];
        tmax[n+i] = a[i];
        tmin[n+i] = a[i];
    }
    bmax(); bmin();
    for (int i = 0; i<n; i++){
        res[i] = bs(i, n-1);
        tres[n+i] = mp(-res[i], i);
    }
    bres();
    cin >> Q;
    while (Q--){
        int l, r;
        cin >> l >> r;
        l--; r--;
        if (res[l]+l-1 >= r) cout << l+1 << " " << r+1 << "\n";
        else{
            int rr = r;
            r = bs2(l, r);
            pii q = qres(l, r);
            if (r < rr) q = get(q, mp(r-rr, r+1));
            cout << q.second+1 << " " << q.second+1-q.first-1 << "\n";
        }
    }
}