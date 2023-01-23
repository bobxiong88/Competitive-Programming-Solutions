#include <bits/stdc++.h>
using namespace std;
#define m 1026
#define n 1026
int s, x, y, a, xa, xb, ya, yb, q;
int LSB(int x){
    return x & (-x);
}
int bit[m][n];
int query(int x, int y){
    int sum = 0;
    for (int xi = x; xi > 0; xi -= LSB(xi)){
        for (int yi = y; yi > 0; yi -= LSB(yi)){
            sum += bit[xi][yi];
        }
    }
    return sum;
}
int qa(int x1, int y1, int x2, int y2){
    return (query(x2, y2) - query(x1-1, y2) - query(x2, y1-1) + query(x1 - 1, y1 - 1));
}
void update(int x, int y, int value){
    for (int xi = x; xi < m; xi += LSB(xi)){
        for (int yi = y; yi < n; yi += LSB(yi)){
            bit[xi][yi] += value;
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);
    while (true){
        cin >> q;
        if (q == 0){
            cin >> s;
        }
        else if (q == 1){
            cin >> x >> y >> a;
            x++; y++;
            update(x, y, a);
        }
        else if (q == 2){
            cin >> xa >> ya >> xb >> yb;
            xa++; ya++; xb++; yb++;
            cout << qa(xa, ya, xb, yb) << "\n";
        }
        else{
            break;
        }
    }
}