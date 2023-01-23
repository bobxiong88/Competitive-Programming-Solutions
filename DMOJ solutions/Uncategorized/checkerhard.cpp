#include <bits/stdc++.h>
using namespace std;
//algorithm from: https://iq.opengenus.org/2d-fenwick-tree/
int M, N, R, C, X, R1, C1, R2, C2, q, v;
int LSB(int x){
    return x & (-x);
}
#define mx 3001
int bit[2][mx][mx];
int grid[mx][mx];
int query(int x, int y, int bit[mx][mx]){
    int sum = 0;
    for (int xi = x; xi > 0; xi -= LSB(xi)){
        for (int yi = y; yi > 0; yi -= LSB(yi))
            sum += bit[xi][yi];
    }
    return sum;
}
int qa(int x1, int y1, int x2, int y2, int bit[mx][mx]){
    return (query(x2, y2, bit) - query(x1-1, y2, bit) - query(x2, y1-1, bit) + query(x1 - 1, y1 - 1, bit));
}
void update(int x, int y, int value, int bit[mx][mx]){
    for (int xi = x; xi <= M; xi += LSB(xi)){
        for (int yi = y; yi <= N; yi += LSB(yi))
            bit[xi][yi] += value;
    }
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(0);
    cin >> M >> N;
    while (true){
        cin >> q;
        if (q == 1){
            cin >> R >> C >> X;
            update(R, C, X-grid[R][C], bit[(R+C)%2]);
            grid[R][C] = X;
        }
        else if (q == 2){
            cin >> R1 >> C1 >> R2 >> C2;
            cout << qa(R1, C1, R2, C2, bit[(R1+C1)%2])-qa(R1, C1, R2, C2, bit[1-(R1+C1)%2]) << "\n";
        }
        else{
            break;
        }
     }
}