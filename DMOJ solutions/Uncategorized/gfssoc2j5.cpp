#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
int mt[1000005][2];
int n, Q, a, b;
string q;
void mb(){
    for (int i = n - 1; i > 0; --i){
        if (mt[i<<1][0] > mt[i<<1|1][0]){
            mt[i][0] = mt[i<<1][0];
            mt[i][1] = mt[i<<1][1];
        }
        else if (mt[i<<1][0] < mt[i<<1|1][0]){
            mt[i][0] = mt[i<<1|1][0];
            mt[i][1] = mt[i<<1|1][1];
        }
        else{
            mt[i][0] = mt[i<<1][0];
            mt[i][1] = mt[i<<1][1] + mt[i<<1|1][1];
        }
    }
}
int mq(int l, int r){
    r++;
    int res = -1;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = max(mt[l++][0], res);
        if (r&1) res = max(mt[--r][0], res);
    }
    return res;
}
int qq(int l, int r, int m){
    r++;
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1){
            if (mt[l++][0] == m) res+=mt[l-1][1];
        }
        if (r&1){
            if (mt[--r][0] == m) res+=mt[r][1];
        }
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);
    cin >> n >> Q;
    n++;
    for(int i = 1; i<n; ++i){
        cin >> a;
        mt[n+i][0] = a;
        mt[n+i][1] = 1;
    }
    mb();
    for(int i = 0; i<Q; i++){
        cin >> a >> b;
        int left = mq(1, a-1);
        int right = mq(b+1, n);
        int m = max(left, right);
        cout << m << " " << qq(1, a-1, m)+qq(b+1, n, m) << "\n";
    }
    return 0;
}