#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int a[n*2];
        int o = 0;
        int e = 0;
        for (int i = 0; i<2*n; i++){
            cin >> a[i];
            if (a[i]%2) o++;
            else e++;
        }
        if (o == e) cout << "Yes\n";
        else cout << "No\n";
    }

}
