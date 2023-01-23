#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define mp make_pair
#define pb push_back
#define int ll
main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i<n; i++){
            cin >> a[i];
        }
        for(int i = 0; i<n-1; i++){
            int m = a[i]*a[i+1];
            a[i] = 1;
            a[i+1] = m;
        }
        int s = 0;
        for (int i = 0; i<n; i++){
            s += a[i];
        }
        cout << s*2022 << "\n";
    }
}
