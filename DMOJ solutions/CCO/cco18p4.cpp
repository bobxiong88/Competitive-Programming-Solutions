#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
int get(int x, int y){
    int v;
    cout << "? " << x << " " << y << endl;
    cin >> v;
    return v;
}
main(){
    int R, C, K, xl, xr, yl, yr, mx, my, mv, xv, yv;
    int cnt = 0;
    cin >> R >> C >> K;
    xl = 1; xr = R;
    yl = 1; yr = C;
    while ((xl < xr-1) || (yl < yr-1)){
        mx = (xl+xr)/2;
        my = (yl+yr)/2;
        mv = get(mx, my);
        xv = get(min(mx+1, R), my);
        yv = get(mx, min(my+1, C));
        if (mv < xv) xr = mx;
        else xl = mx;
        if (mv < yv) yr = my;
        else yl = my;
    }
    int v = get(xr, yr);
    cout << "! " << v << endl;
    return 0;
}