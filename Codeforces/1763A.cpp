#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i<n; i++){
            cin >> a[i];
        }
        int ans = 0;
        for (int x = 0; x<12; x++){
            int o = 0;
            int z = 0;
            for (int i = 0; i<n; i++){
                if ((a[i]>>x)&1) o++;
                else z++;
            }
            if (!(o==0||z==0)){
                ans += 1<<x;
            }
        }
        cout << ans << "\n";
    }
}
