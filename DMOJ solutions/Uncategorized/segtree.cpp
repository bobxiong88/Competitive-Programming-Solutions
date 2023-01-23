#include <bits/stdc++.h>
using namespace std;
#define n 100005
#define mx 2000000000
int t[n*2];
int N, M, a,b;
string q;
void modify(int p, int value){
    for (t[p += n] = value; p > 1; p >>= 1) t[p>>1] = min(t[p], t[p^1]);
}
int query(int l, int r){
    r++;
    int res = mx;
    for (l += n, r += n; l < r; l>>=1, r>>=1){
        if (l&1) res = min(res, t[l++]);
        if (r&1) res = min(res, t[--r]);
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    memset(t, mx, 2*n);
    cin >> N >> M;
    for (int i = 0; i < N; i++){
        cin >> a;
        modify(i, a);
    }
    while (M--){
        cin >> q >> a >> b;
        if (q == "Q")
            cout << query(a,b) << "\n";
        else
            modify(a,b);
    }
}