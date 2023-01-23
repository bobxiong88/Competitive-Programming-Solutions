// i hate ds

#include <bits/stdc++.h>
using namespace std;
#define big 4000000
int t[big*2][2];
int n;
void update(int p, int v){
    for (t[p+=n][0] = v; p>1; p>>=1){
        t[p>>1][0] = max(t[p][0], t[p^1][0]);
        if (t[p][0] > t[p^1][0]) t[p>>1][1] = t[p][1];
        else t[p>>1][1] = t[p^1][1];
    }
}
int win(int v){
    int res = 0;
    int p = v;
    for (p+=n; p>1; p>>=1){
        if (v == t[p>>1][1]){
            res++;
        }
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M, x, k, S;
    string T;
    cin >> N >> M;
    n = pow(2,N);
    for (int i = 0; i<n; i++){
        cin >> x;
        t[i+n][1] = i;
        update(i, x);
    }
    while (M--){
        cin >> T;
        if (T == "R"){
            cin >> k >> S;
            k--;
            update(k, S);
        }
        else if (T == "W"){
            cout << t[1][1]+1 << "\n";
        }
        else{
            cin >> k;
            k--;
            cout << win(k) << "\n";
        }
    }
}