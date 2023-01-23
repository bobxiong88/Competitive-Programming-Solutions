#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

const int mx  = int(2e5)+5;
int t[2*mx];

void build(){
    for (int i = mx-1; i>0; --i) t[i] = max(t[i<<1],t[i<<1|1]);
}
int query(int l, int r){
    r++;
    int res = -mx;
    for (l += mx, r+=mx; l<r; l>>=1, r>>=1){
        if (l&1) res = max(res, t[l++]);
        if (r&1) res = max(res, t[--r]);
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    for (int i = 0; i<2*mx; i++) t[i] = -mx;
    int N, Q;
    string S;
    cin >> N >> Q;
    cin >> S;
    vector<int> psl, psr;
    psl.pb(0); psr.pb(0);
    for (int i = 0; i<N; i++){
        psl.pb(psl[i]+(S[i]=='('));
        psr.pb(psr[i]+(S[i]==')'));
        t[mx+i+1] = psr[i+1]-psl[i+1];
    }
    //for (int i = 1; i<=N; i++) cout << psl[i] << " "; cout << "\n";
    //for (int i = 1; i<=N; i++) cout << psr[i] << " "; cout << "\n";
    //for (int i = 1; i<=N; i++) cout << t[mx+i] << " "; cout << "\n";
    build();
    while (Q--){
        int L, R;
        cin >> L >> R;
        int res = query(L, R)-psr[L-1]+psl[L-1];
        //cout << "res: " << res << "\n";
        if (res <= 0){
            cout << "YES\n";
        }
        else{
            if (res <= (psr[R]-psr[L-1])-(psl[R]-psl[L-1])){
                cout << "YES\n";
            }
            else{
                cout << "NO\n";
            }
        }
    }
}