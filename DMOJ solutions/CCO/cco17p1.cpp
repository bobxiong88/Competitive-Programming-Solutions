#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>

int main(){
    int K, N, x, n;
    vector<pii> edge;
    cin >> K;
    N = 1;
    while (K != 0){
        n = floor((1+sqrt(1+8*K))/2);
        x = (n*n-n)/2;
        K -= x;
        for (int i = 0; i<n-1; i++){
            edge.pb(mp(N+i, N+i+1));
        }
        edge.pb(mp(N+n-1, N));
        edge.pb(mp(N+n-1,N+n));
        N = N+n;
    }
    cout << N << " " << edge.size() << "\n";
    for (auto [a,b]: edge){
        cout << a << " " << b << "\n";
    }
}