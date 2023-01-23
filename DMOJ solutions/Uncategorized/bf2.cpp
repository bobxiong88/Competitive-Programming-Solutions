#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx int(1e6)+5
const int p = 31;
const int m = int(1e9)+7;
string s;
int h[mx], pw[mx];
int get(int a, int b){
    if (a) return (h[b]-h[a-1]*pw[b-a+1]+m*m)%m;
    return h[b];
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int K;
    cin >> s;
    cin >> K;
    int N = s.length();
    pw[0] = 1;
    h[0] = s[0];
    for (int i = 1; i<N; i++){
        pw[i] = (pw[i-1]*p)%m;
        h[i] = (h[i-1]*p+s[i])%m;
    }
    int x = 0;
    for (int i = 0; i<N-K+1; i++){
        int l = 0;
        int r = K;
        int d = 0;
        while (l <= r){
            int m = (l+r)/2;
            if (get(x, x+m-1) == get(i, i+m-1)){
                d = m;
                l = m+1;
            }
            else{
                r = m-1;
            }
        }
        if (d == K) continue;
        if (s[x+d] > s[i+d]) x = i;
    }
    for (int i = x; i<x+K; i++){
        cout << s[i];
    }
    cout << "\n";
}