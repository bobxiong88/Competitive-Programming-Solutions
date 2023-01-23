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
        string s;
        cin >> s;
        int a = s[0]-48;
        int b = s[2]-48;
        cout << a+b << "\n";
    }
}
