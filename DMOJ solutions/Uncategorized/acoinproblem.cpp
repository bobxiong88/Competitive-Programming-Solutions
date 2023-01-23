#include <bits/stdc++.h>
using namespace std;
#define len 10001
struct item{
    int l,c,k;
};
bool comp(const item &a, const item &b){
    return a.l < b.l;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int N, V, x, l, c, k;
    cin >> N >> V;
    int coins[N];
    int ans[V];
    vector<item> query;
    for(int i = 0; i<N; i++) cin >> coins[i];
    for(int i = 0; i<V; i++){
        cin >> c >> l;
        query.push_back({l-1, c, i});
    }
    sort(query.begin(), query.end(), comp);
    x = 0;
    int dp[len];
    for(int i = 0; i<len; i++) dp[i] = -1;
    dp[0] = 0;
    for(int i = 0; i<N; i++){
        for(int j = 1; j<len; j++){
            if (coins[i] <= j){
                int res = dp[j-coins[i]];
                if (res != -1 && ((res + 1) < dp[j] || dp[j] == -1))
                    dp[j] = res + 1;
            }
        }
        while (query[x].l == i){
            ans[query[x].k] = dp[query[x].c];
            x++;
            if (x == V){
                for(int i = 0; i<V; i++){
                    cout << ans[i] << "\n";
                }
                return 0;
            }

        }
    }
}