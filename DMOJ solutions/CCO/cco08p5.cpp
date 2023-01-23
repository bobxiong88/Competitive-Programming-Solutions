#include <bits/stdc++.h>
using namespace std;
#define mx 2000000000
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int N, V, k, c;
    cin >> N;
    V = 0;
    vector<pair<int,int>> a(N);
    for(int i = 0; i<N; i++){
        cin >> k >> c;
        V += k*c;
        a.push_back(make_pair(k,c));
    }
    int dp[V+1];
    for(int i = 0; i<=V; i++) dp[i] = mx;
    dp[0] = 0;
    for(auto p: a){
        k = p.first; c = p.second;
        int cnt[V+1] = {0};
        for (int i = 1; i<=V; i++){
            if (c <= i){
                int res = dp[i-c];
                if (res != mx && res + 1 < dp[i] && cnt[i-c]+1 <= k){
                    dp[i] = res + 1;
                    cnt[i] = cnt[i-c] + 1;
                }
            }
        }
    }
    int m = mx;
    for (int i = 0; i<=V; i++){
        if (dp[i] != mx)
            m = min(m, abs(V-i*2));
    }
    cout << m;
}