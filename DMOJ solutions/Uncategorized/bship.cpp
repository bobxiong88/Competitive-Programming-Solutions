#include <bits/stdc++.h>
#include <iomanip>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int n,m,s;
    char a;
    double c;
    cin >> n >> m >>s;
    for (int i = 0; i<n; i++){
        int y = min(i, n-i-1);
        if (y >= s-1) y = s;
        else y++;
        for (int j = 0; j<m; j++){
            cin >> a;
            if (a == '.') continue;
            int x = min(j, m-j-1);
            if (x >= s-1) x = s;
            else x++;
            c += min(x,m-s+1)*min(y,m-s+1);
        }
    }
    cout << std::fixed << std::setprecision(8) << c/((m-s+1)*(n-s+1)) << "\n";
}