// build 21 BITs
// query 1: subtract 1 from bit[val[a]][a] and add 1 to bit[b][a], val[a] = b
// query 2: iterate 20-->0, find sum each time, when sum >= c, print val
#include <bits/stdc++.h>
using namespace std;
const int mx = int(3e5)+5;
int bit[21][mx];
int val[mx];
int lsb(int x){
    return x&(-x);
}
int qry(int t, int x){
    int sum = 0;
    for (int i = x; i > 0; i -= lsb(i))
        sum += bit[t][i];
    return sum;
}
void upd(int t, int x, int v){
    for (int i = x; i < mx; i += lsb(i))
        bit[t][i] += v;
}
int get_sum(int t, int l, int r){
    return qry(t, r)-qry(t, l-1);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M;
    cin >> N >> M;
    for (int i = 1; i<= N; i++){
        cin >> val[i];
        upd(val[i], i, 1);
    }
    while (M--){
        int q;
        cin >> q;
        if (q == 1){
            int a, b;
            cin >> a >> b;
            upd(val[a], a, -1);
            val[a] = b;
            upd(val[a], a, 1);
        }
        else{
            int l, r, c;
            cin >> l >> r >> c;
            int sum = 0;
            for (int i = 20; i >= 0; i--){
                sum += get_sum(i, l, r);
                if (sum >= c){
                    cout << i << "\n";
                    break;
                }
            }
        }
    }

}