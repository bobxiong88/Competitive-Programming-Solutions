#include <bits/stdc++.h>
using namespace std;
//algorithm from: https://iq.opengenus.org/2d-fenwick-tree/
int M, N, R, C, X, R1, C1, R2, C2, q;
int LSB(int x){
    return x & (-x);
}
int bitOdd[3001][3001];
int bitEven[3001][3001];
int grid[3001][3001];
int query(int x, int y, int bit[][3001]){
    int sum = 0;
    for (int xi = x; xi > 0; xi -= LSB(xi)){
        for (int yi = y; yi > 0; yi -= LSB(yi)){
            sum += bit[xi][yi];
        }
    }
    return sum;
}
int qa(int x1, int y1, int x2, int y2, int bit[][3001]){
    return (query(x2, y2, bit) - query(x1-1, y2, bit) - query(x2, y1-1, bit) + query(x1 - 1, y1 - 1, bit));
}
void update(int x, int y, int value, int bit[][3001]){
    for (int xi = x; xi <= M; xi += LSB(xi)){
        for (int yi = y; yi <= N; yi += LSB(yi)){
            bit[xi][yi] += value;
        }
    }
}
main(){
     for (int i = 0; i <= M; i++){
        for (int j = 0; j <= N; j++){
            bitEven[i][j] = 0;
            bitOdd[i][j] = 0;
            grid[i][j] = 0;
        }
     }
     cin >> M >> N;
     while (true){
        cin >> R >> C >> X;
        if (!R && !C){
            break;
        }
        R = min(M, R);
        C = min(N, C);
        int v = X-grid[R][C];
        grid[R][C] = X;
        if ((R + C)%2){
            update(R, C, v, bitOdd);
            update(R, C, -v, bitEven);
        }
        else{
            update(R, C, v, bitEven);
            update(R, C, -v, bitOdd);
        }
    }
    while (true){
        cin >> R1 >> C1 >> R2 >> C2;
        R1 = min(M, R1);
        R2 = min(M, R2);
        C1 = min(N, C1);
        C2 = min(N, C2);
        if (!R1 && !R2){
            break;
        }
        if ((R1 + C1)%2){
            cout << qa(R1, C1, R2, C2, bitOdd) << "\n";
        }
        else{
            cout << qa(R1, C1, R2, C2, bitEven) << "\n";
        }
    }
}
/*
3 3
1 1 1 1
1 1 2 2
1 1 3 3
1 2 1 4
1 2 2 5
1 2 3 6
1 3 1 7
1 3 2 8
1 3 3 9
*/