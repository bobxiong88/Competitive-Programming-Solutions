#include <bits/stdc++.h>
using namespace std;
#define mx int(1e5)+5
int bit[2][mx];
int lsb(int x){
    return x&(-x);
}
int query(int x, int k){
    int res = 0;
    for (int i = x; i > 0; i-=lsb(i)) res += bit[k][i];
    return res;
}
void update(int x, int v, int k){
    for (int i =x; i<mx; i+=lsb(i)) bit[k][i] += v;
}
int qa(int l, int r, int k){
    return query(r, k)- query(l-1, k);
}
int a[mx];
int pp[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, x;
    cin >> N;

    for (int i = 1; i<=N; i++){
        cin >> a[i];
        pp[a[i]] = i;
    }
    for (int i = 1; i<=N; i++){
        int k = i%2;
        if (k){
            x = int(i/2)+1;
        }
        else{
            x = N-int((i-1)/2);
        }
        //cout << "x " << x << "\n";
        int p = pp[x];
        update(p, 1, k);
        int pos = p;
        pos += qa(p+1, N, 1);
        pos -= qa(1, p-1, 0);
        //cout << p << " " << pos << " " << k <<"\n";
        if (k){
            cout << pos-x << "\n";
        }
        else{
            cout << x-pos << "\n";
        }
    }
}