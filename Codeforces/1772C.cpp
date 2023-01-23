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
        int k,n;
        cin >> k >> n;
        int x = 1;
        cout << x << " ";
        int d = 1;
        for (int i = 1; i<k; i++){
            int nxt = min(d+x, n-k+i+1);
            cout << nxt << " ";
            x = nxt;
            d++;
        }
        cout << "\n";
    }
}
