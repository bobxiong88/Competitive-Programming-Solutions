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
        int a[n+1];
        int f = 0;
        int s = 0;
        int ti = 0;
        for (int i = 1; i<=n; i++){
            cin >> a[i];
            if (i != a[i]){
                f++;
            }
            if (n-i+1 != a[i]){
                s++;
            }
            if (i != a[i]&&n-i+1 != a[i]){
                f--; s--; ti++;
            }
        }
        //cout << f<<" " << s << " " << ti<< "\n";
        if (f-ti<=s && s-ti < f){
            cout << "Tie";
        }
        else if (f<=s){
            cout << "First";
        }
        else{
            cout << "Second";
        }
        cout<<"\n";
    }
}
