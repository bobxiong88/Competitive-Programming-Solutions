#include <bits/stdc++.h>
using namespace std;
int a[450][200001];
vector<vector<int>> b(450);
int n, u, v, x, l, r, Q, q, s, e;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);
    cin >> n >> Q;
    int s = floor(pow(n, 0.5));
    int c = 0;
    for (int i = 0; i<n; i++){
        cin >> e;
        b[c].push_back(e);
        if (b[c].size() == s) c++;
    }
    for (int i = 0; i<450; i++){
        for (int j = 0; j<200001; j++){
            a[i][j] = 0;
        }
    }

    for (int i = 0; i<=c; i++){
        for (int x: b[i]){
            for (int j = 1; j<=floor(pow(x,0.5)); j++){
                if (x%j==0){
                    if (j*j != x) a[i][j]++;
                    a[i][x/j]++;
                }
            }
        }
    }
    while (Q--){
        cin >> q;
        if (q == 1){
            cin >> l >> r >> x;
            l--; r--;
            int s1 = floor(l/s);
            int s2 = l%s;
            int e1 = floor(r/s);
            int e2 = r%s;
            int ans = 0;
            int p = b[s1].size();
            if (s1 == e1){
                p = e2+1;
            }
            //cout << p << "\n";
            for (int i = s2; i<p; i++){
                if (b[s1][i]%x==0) ans++;
                c = i;
            }
            //cout << c << " pooo " <<s2 << "\n";
            p = 0;
            if (s1 == e1){
                p = c+1;
            }
            //cout << ans << "\n";
            for (int i = s1+1; i<e1; i++){
                ans += a[i][x];
                //cout << "a at " << i << " is: " << a[i][x] << "\n";
            }
            //cout << ans << "\n";
            for (int i = e2; i>=p; i--){
                if (b[e1][i]%x==0) ans++;
            }
            cout << ans << "\n";
            //cout << "_______________________________\n";
        }
        else {
            cin >> u >> x;
            u--;
            int i = floor(u/s);
            int j = u%s;
            int curr = b[i][j];
            for (int d = 1; d<=floor(pow(curr, 0.5)); d++){
                if (curr%d==0){
                    if (d*d != curr) a[i][d]--;
                    a[i][curr/d]--;
                }
            }
            b[i][j] = x;
            for (int d = 1; d<=floor(pow(x, 0.5)); d++){
                if (x%d==0){
                    if(d*d != x) a[i][d]++;
                    a[i][x/d]++;
                }
            }
        }
    }
}
/*
9 10
1 2 3 4 5 6 7 8 9
1 4 6 2
*/
/*
13 30
1 1 1 1 1 1 1 1 1 1 1 1 1
13 30
1 2 3 4 5 6 7 8 9 10 11 12 13
2 1 1
2 2 1
2 3 1
2 4 1
2 5 1
2 6 1
2 7 1
2 8 1
2 9 1
2 10 1
2 11 1
2 12 1
2 13 1
1 1 12 1
1 4 13 1
1 4 12 1
1 4 10 1
*/