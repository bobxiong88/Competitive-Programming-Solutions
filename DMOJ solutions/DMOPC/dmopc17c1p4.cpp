#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int N, H, a, g, h, q, t;
    cin >> N >> H;
    int curr[H+1][2];
    int pre[H+1][2];
    for(int i = 0; i<H+1; i++){
        pre[i][0] = 0;
        pre[i][1] = 0;
        curr[i][0] = 0;
        curr[i][1] = 0;
    }
    while (N--){
        cin >> g >> h >> q >> t;
        for(int j = 1; j<H+1; j++){
            curr[j][0] = max(pre[j][0], pre[j][1]);
            a = 0;
            if (j >= h)
                a = curr[j-h][0]+g;
            if (j >= h+t)
                a = max(a, curr[j-t][1]+q);
            curr[j][1] = a;
        }
        for(int i = 0; i<H+1; i++){
            pre[i][0] = curr[i][0];
            pre[i][1] = curr[i][1];
        }
    }
    cout << max(curr[H][0], curr[H][1]);
}