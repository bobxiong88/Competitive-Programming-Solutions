#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<pair<int,int>> v;
    int N, P, a, b, ans, p;
    cin >> N >> P;
    ans = 0;
    p = 1;
    for (int i = 1; i<=N; i++){
        cin >> a >> b;
        if (i != P){
            if (a < b) continue;
            v.push_back(make_pair(b, a));
            continue;
        }
        ans += a;
    }
    sort(v.begin(), v.end());
    for (auto [b, a]: v){
        ans -= b;
        if (ans < 0){
            ans += b;
            break;
        }
        ans += a;
        p++;
    }
    cout << ans << "\n" << p << "\n";
}