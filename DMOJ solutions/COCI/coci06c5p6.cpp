#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
int v(char c){
    return int(c)-96;
}
int t1[200003];
int t2[200003];
string s;
int L, l, r, n, ans, hs1, m1, p1, hs2, m2, p2;
bool balls;
main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    ans = 0; p1 = 131; m1 = 200003; p2 = 51; m2 = 2147483647;
    cin >> L >> s;
    l = 0;
    r = L;
    t1[0] = 1;
    t2[0] = 1;
    for (int i = 1; i<L; i++){
        t1[i] = p1*t1[i-1]%m1;
        t2[i] = p2*t2[i-1]%m2;
    }
    while (l <= r){
        n = (l+r)/2;
        hs1 = 0;
        hs2 = 0;
        for (int i = L-n; i<L; i++){
            hs1 += v(s[i])*t1[i-L+n];
            hs1 %= m1;
            hs2 += v(s[i])*t2[i-L+n];
            hs2 %= m2;
        }
        vector<vector<int>> cumbucket(m1);
        cumbucket[hs1].push_back(hs2);
        balls = false;
        for (int i = L-1; i > n-1; i--){
            hs1 = hs1-((v(s[i])*t1[n-1])%m1)+m1;
            hs1 = (hs1*p1+v(s[i-n]))%m1;
            hs2 = hs2-((v(s[i])*t2[n-1])%m2)+m2;
            hs2 = (hs2*p2+v(s[i-n]))%m2;
            if (count(cumbucket[hs1].begin(), cumbucket[hs1].end(), hs2)){
                ans = max(ans, n);
                l = n+1;
                balls = true;
                break;
            }
            else{
                cumbucket[hs1].push_back(hs2);
            }
        }
        if (balls) continue;
        r = n-1;
    }
    cout << ans;
    return 0;
}