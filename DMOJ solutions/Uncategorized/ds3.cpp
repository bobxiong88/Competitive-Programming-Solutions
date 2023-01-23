#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
int gt[200002];
int mt[200002][2];
int n, Q, a, b;
string q;
int gcd(int a, int b){
    if (a == 0)
        return b;
    return gcd(b%a, a);
}
void gb(){
    for (int i = n - 1; i > 0; --i) gt[i] = gcd(gt[i<<1], gt[i<<1|1]);
}
void gu(int p, int value){
    for (gt[p += n] = value; p > 1; p >>= 1) gt[p>>1] = gcd(gt[p], gt[p^1]);
}
int gq(int l, int r){
    r++;
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = gcd(res, gt[l++]);
        if (r&1) res = gcd(res, gt[--r]);
    }
    return res;
}
void mb(){
    for (int i = n - 1; i > 0; --i){
        if (mt[i<<1][0] < mt[i<<1|1][0]){
            mt[i][0] = mt[i<<1][0];
            mt[i][1] = mt[i<<1][1];
        }
        else if (mt[i<<1][0] > mt[i<<1|1][0]){
            mt[i][0] = mt[i<<1|1][0];
            mt[i][1] = mt[i<<1|1][1];
        }
        else{
            mt[i][0] = mt[i<<1][0];
            mt[i][1] = mt[i<<1][1] + mt[i<<1|1][1];
        }
    }
}
void mu(int p, int value){
    for (mt[p += n][0] = value; p > 1; p >>= 1){
        if (mt[p][0] < mt[p^1][0]){
            mt[p>>1][0] = mt[p][0];
            mt[p>>1][1] = mt[p][1];
        }
        else if (mt[p][0] > mt[p^1][0]){
            mt[p>>1][0] = mt[p^1][0];
            mt[p>>1][1] = mt[p^1][1];
        }
        else {
            mt[p>>1][0] = mt[p][0];
            mt[p>>1][1] = mt[p][1] + mt[p^1][1];
        }
    }
}
int mq(int l, int r){
    r++;
    int res = 2000000000;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = min(mt[l++][0], res);
        if (r&1) res = min(mt[--r][0], res);
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
        gt[n+i] = a;
        mt[n+i][0] = a;
        mt[n+i][1] = 1;
    }
    gb(); mb();
    for(int i = 0; i<Q; i++){
        cin >> q >> a >> b;
        if(q == "C"){
            gu(a,b); mu(a,b);
        }
        else if(q == "M"){
            cout << mq(a, b) << "\n";
        }
        else if(q== "G"){
            cout << gq(a, b) << "\n";
        }
        else{
            //cout << gq(a,b) << "\n";
            cout << qq(a, b, gq(a,b)) << "\n";
        }
    }
    return 0;
}