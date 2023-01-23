#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N, Q, q, i, j, a, b, h;
    cin >> N;
    int A[N];
    for(int i = 0; i<N; i++){
        cin >> A[i];
    }
    cin >> Q;
    for(int t = 0; t<Q; t++){
        cin >> q;
        if(q==1){
            cin >> i >> j >> a >> b;
            int c = 0;
            for(int x = i; x<=j; x++){
                if(a<=A[x] && A[x]<=b){
                    c++;
                }
            }
            cout << c << "\n";
        }
        else{
            cin >> i >> h;
            A[i] = h;

        }
    }
}