#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int N ,M, mx, x, y;
    mx = 1000000000;
    int first[1000005];
    int last[1000005];
    cin >> N >> M;
    for (int i = 0; i<1000005; i++){
        first[i] = mx;
        last[i] = -1;
    }
    for (int i = 0; i<N; i++){
        cin >> x;
        first[x] = min(first[x], i);
        last[x] = max(last[x], i);
    }
    int ans = 0;
    for (int i = 0; i<M; i++){
        cin >> x >> y;
        x = first[x];
        y = last[y];
        if (x == mx) continue;
        if (y == -1) continue;
        ans = max(ans, y-x+1);
    }
    cout << ans << "\n";
}