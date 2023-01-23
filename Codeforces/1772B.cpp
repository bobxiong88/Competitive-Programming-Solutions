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
        int a[4];
        string ans = "NO";
        cin >> a[0] >> a[1] >> a[3] >> a[2];
        for (int j = 0;j<4; j++){
            int b[4];
            for (int i = 0; i<4; i++){
                b[i] = a[(i+1)%4];
            }
            if (b[0]<b[1] && b[0] < b[3] && b[1] < b[2] && b[3]<b[2]){
                ans = "YES";
            }
            for (int i = 0; i<4; i++) a[i] = b[i];
        }
        cout << ans << "\n";
    }
}
