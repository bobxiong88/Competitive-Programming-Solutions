#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, Q;
    cin >> N >> Q;
    int a[N];
    int log[N+1];
    log[1] = 0;
    for(int i = 2; i<=N; i++)
        log[i] = log[i/2]+1;

    for(int i = 0;i<N;i++)
        cin >> a[i];
    int K = 17;
    int st[N][K+1];
    int st2[N][K+1];
    for(int i = 0; i< N; i++){
        st[i][0] = a[i];
        st2[i][0] = -a[i];
    }

    for(int j = 1; j<= K; j++){
        for(int i = 0; i+ (1<<j) <= N; i++){
            st[i][j] = min(st[i][j-1], st[i+(1<<(j-1))][j-1]);
            st2[i][j] = min(st2[i][j-1], st2[i+(1<<(j-1))][j-1]);
        }
    }
    for(int i = 0; i<Q; i++){
        int L, R;
        cin >> L >> R;
        L-=1;
        R-=1;
        int j = log[R-L+1];
        int small = min(st[L][j], st[R-(1<<j)+1][j]);
        int large = -min(st2[L][j], st2[R-(1<<j)+1][j]);
        cout << large-small << "\n";
    }
}