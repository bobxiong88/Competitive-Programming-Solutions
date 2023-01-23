#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast")
#define mx 500005
int arr[mx] = {0};
vector<map<int,int>> t(mx*2);
int n;
void build(){
    for (int i = n-1; i>0; --i){
        int a = 0;
        int b = 0;
        if(t[i<<1].count(0)) a = t[i<<1][0];
        if(t[i<<1|1].count(0)) b = t[i<<1|1][0];
        t[i].insert({0, a+b});
    }
}
void update(int p, int a, int b){
    p += n;
    if (!t[p].count(b)) t[p].insert({b, 1});
    else t[p][b]++;
    t[p][a]--;
    for (; p > 1; p >>= 1){
        if (!t[p>>1].count(b)) t[p>>1].insert({b, 0});
        if (!t[p^1].count(a)) t[p>>1][a] = t[p][a];
        else t[p>>1][a] = t[p][a] + t[p^1][a];
        if (!t[p^1].count(b)) t[p>>1][b] = t[p][b];
        else t[p>>1][b] = t[p][b] + t[p^1][b];
        if (!t[p][a]) t[p].erase(a);
    }
}
int query(int l, int r, int x){
    r++;
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1){
        if (l&1){
            if(t[l].count(x)) res += t[l][x];
            l++;
        }
        if (r&1){
            r--;
            if(t[r].count(x)) res += t[r][x];
        }
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int Q, q, x, l, r;
    cin >> n >> Q;
    for (int i = n+1; i<=n*2; i++) t[i].insert({0, 1});
    build();
    while (Q--){
        cin >> q;
        if (q == 1){
            cin >> x;
            update(x, arr[x], arr[x]+1);
            arr[x] += 1;
        }
        else if (q == 2){
            cin >> x;
            update(x, arr[x], arr[x]-1);
            arr[x] -= 1;
        }
        else{
            cin >> l >> r >> x;
            cout << query(l, r, x) << "\n";
        }
    }
}