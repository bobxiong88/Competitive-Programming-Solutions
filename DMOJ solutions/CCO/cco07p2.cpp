#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll

main(){
    int n, tb[6];
    vector<int> a(6);
    bool found = false;
    int p = 31;
    int m = pow(2,64);
    tb[0] = p;
    for (int i = 1; i<6;i++){
        tb[i] = (tb[i-1]*p)%m;
    }
    unordered_set<int> prev;
    cin >> n;
    while (n--){
        for (int i = 0; i<6; i++){
            cin >> a[i];
        }
        int hs1 = 0;
        for (int i = 0; i<6; i++){
            int hs = 0;
            for (int j = 0; j<6;j++){
                hs += a[(i+j)%6]*tb[j];
                hs %= m;
            }
            if (hs >= hs1) hs1 = hs;
        }
        reverse(a.begin(), a.end());
        int hs2 = 0;
        for (int i = 0; i<6; i++){
            int hs = 0;
            for (int j = 0; j<6;j++){
                hs += a[(i+j)%6]*tb[j];
                hs %= m;
            }
            if (hs >= hs2) hs2 = hs;
        }
        if (prev.count(hs1) || prev.count(hs2)){
            found = true;
            break;
        }
        prev.insert(hs1); prev.insert(hs2);
    }
    if (found) cout << "Twin snowflakes found.\n";
    else cout << "No two snowflakes are alike.\n";
}