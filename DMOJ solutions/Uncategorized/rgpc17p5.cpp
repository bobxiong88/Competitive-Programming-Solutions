#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int n, m;
    string s;
    string k;
    cin >> n >> m;
    cin >> s >> k;
    m--;
    int row[n+1];
    for(int i = 0;i<n+1; i++) row[i] = i;
    int a = 0;
    for(int j = 1; j<=m; j++){
        int nr[n+1];
        for(int i = 0; i<=n; i++) nr[i] = i;
        for(int i = 1; i<=n; i++){
            int v = 0;
            if (s[i-1] != k[j-1]) v = 1;
            if (i-1 == 0) nr[i-1] = j;
            nr[i] = min(min(row[i]+1, nr[i-1]+1), row[i-1]+v);
        }
        a += nr[n];
        for(int i = 0; i<=n; i++) row[i] = nr[i];
    }
    cout << a;
}