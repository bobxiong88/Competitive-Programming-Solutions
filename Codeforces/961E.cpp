// how many pairs of (i,j) such that i < j, j <= a_i && i <= a_j
// essentially, all a_k >= n can be turned into a_k = n wlog
// for each i count how many values after a_i has value greater or equal to i
// position array for each unique of a_k, decrement count array at those positions once i exceeds value
// maintain bit on the number of elements greater than i
#include <bits/stdc++.h>
using namespace std;
const int mx = int(2e5)+5;
int bit[mx];
int a[mx];
vector<int> pos[mx];
int lsb(int x){
    return x&(-x);
}
int qry(int x){
    int sum = 0;
    for (int i = x; i > 0; i -= lsb(i))
        sum += bit[i];
    return sum;
}
void upd(int x, int v){
    for (int i = x; i < mx; i += lsb(i))
        bit[i] += v;
}
int get_sum(int l, int r){
    return qry(r)-qry(l-1);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int n;
    cin >> n;
    for (int i = 1; i<=n; i++){
        cin >> a[i];
        if (a[i] > n) a[i] = n;
        pos[a[i]].push_back(i);
        upd(i, 1);
    }
    long long ans = 0;
    for (int i = 1; i<=n; i++){
        if (i+1 <= a[i]) ans += get_sum(i+1, a[i]);
        for (auto j: pos[i]){
            upd(j, -1);
        }
    }
    cout << ans << "\n";
}
