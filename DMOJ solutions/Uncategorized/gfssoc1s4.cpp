#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define n 251
int N, Q, x, y, z, a;
string q;
int LSB(int x){
    return x & (-x);
}
int bit[n][n][n];
int cube[n][n][n];
int query(int x, int y, int z){
    int sum = 0;
    for (int xi = x; xi > 0; xi -= LSB(xi)){
        for (int yi = y; yi > 0; yi -= LSB(yi)){
            for (int zi = z; zi > 0; zi -= LSB(zi)){
                sum += bit[xi][yi][zi];
            }
        }
    }
    return sum;
}
int qa(int x1, int y1, int z1, int x2, int y2, int z2){
    return query(x2, y2, z2) - query(x1-1, y2, z2) - query(x2, y1-1, z2) - query(x2, y2, z1-1) + query(x2, y1 - 1, z1 - 1) + query(x1 - 1, y2, z1 - 1) + query(x1 - 1, y1 - 1, z2) - query(x1-1, y1-1, z1-1);
}
void update(int x, int y, int z, int value){
    for (int xi = x; xi < n; xi += LSB(xi)){
        for (int yi = y; yi < n; yi += LSB(yi)){
            for (int zi = z; zi < n; zi += LSB(zi)){
                bit[xi][yi][zi] += value;
            }
        }
    }
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    cin >> Q;
    int ans = 0;
    while (Q--){
        cin >> q;
        if (q == "C"){
            cin >> x >> y >> z >> a;
            //update(x, y, z, a - qa(x,y,z,x,y,z));
            update(x, y, z, a - cube[x][y][z]);
            cube[x][y][z] = a;
        }
        else{
            int x1, y1, z1, x2, y2, z2;
            cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
            ans += qa(x1, y1, z1, x2, y2, z2);
        }
    }
    cout << ans << "\n";
}