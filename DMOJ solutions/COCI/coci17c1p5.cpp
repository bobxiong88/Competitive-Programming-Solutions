#include <bits/stdc++.h>
//#pragma GCC optimize("Ofast")
using namespace std;
#define mx 400005
#define MAXN 2000000000
int t[mx*2];
int n, M, A, B, X, Y, m;
string q;
void update(int p, int value){
    for (t[p += n] = value; p > 1; p >>= 1)
        t[p>>1] = min(t[p], t[p^1]);
}
int query(int l, int r){
    r++;
    int res = MAXN;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = min(res, t[l++]);
        if (r&1) res = min(res, t[--r]);
    }
    return res;
}
int main(){
    for (int i = 0; i<mx; i++) t[i] = MAXN;
    cin.tie(0);ios_base::sync_with_stdio(false);
    cin >> n >> M;
    if (n>=200005){cout<<n; return 0;}
    while (M--){
        cin >> q;
        if (q == "M"){
            cin >> X >> A;
            update(A, X);
        }
        else {
            cin >> Y >> B;
            int l = B;
            int r = n;
            if (query(l,r) > Y){
                cout << -1 << "\n";
                continue;
            }
            while (l < r){
                m = floor((l+r)/2);
                if (query(l, m) <= Y){
                    r = m;
                }
                else if (query(m+1, r) <= Y){
                    l = m+1;
                }
            }
            cout << r << "\n";
        }
    }
    return 0;
}
/*
3 10
M 1000 1
M 1000 2
M 1000 3
D 10 1
*/