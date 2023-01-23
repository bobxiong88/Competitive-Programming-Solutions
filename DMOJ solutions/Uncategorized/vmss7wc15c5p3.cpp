#include<bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx 2005
int tree[mx][mx];
int LSB(int x){
    return x & (-x);
}
int query(int x, int* bit){
    int sum = 0;
    for (int i = x; i > 0; i -= LSB(i))
        sum += bit[i];
    return sum;
}
void update(int x, int value, int* bit){
    for (int i = x; i < mx; i += LSB(i))
        bit[i] += value;
}
int qa(int x1, int x2, int* bit){
    return query(x2, bit) - query(x1-1, bit);
}
int N, q, r, c, x, ans;
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(0);
    cin >> N;
    ans = 0;
    while (N--){
        cin >> q >> r >> c >> x;
        if (q == 1)
            update(c, x, tree[r+c]);
        else
            ans += qa(c, c+x, tree[r+c]);
    }
    cout << ans % 1000000007 << "\n";
}