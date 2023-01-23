#include <bits/stdc++.h>
#include <string>
using namespace std;
#define mp make_pair
#define pb push_back
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i<n; i++) cin >> a[i];
        int l = 0;
        int u = 1e9;
        for (int i = 0; i<n-1; i++){
            if (a[i] > a[i+1]){
                l = max(l, (a[i]+a[i+1])/2 + (a[i]+a[i+1])%2);
            }
            else if (a[i] < a[i+1]){
                u = min(u, (a[i]+a[i+1])/2);
            }
        }
        if (l <= u){
            cout << l << "\n";
        }
        else{
            cout << -1 << "\n";
        }
    }
}
