#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
struct pnt{
    int x, y, z, v, r;
};
struct pt{
    int x, y, z;
};
pt sub(pt a, pt b){
    return {a.x-b.x, a.y-b.y, a.z-b.z};
}
pt cross(pt a, pt b){
    int ta = a.y*b.z-a.z*b.y;
    int tb = a.z*b.x-a.x*b.z;
    int tc = a.x*b.y-a.y*b.x;
    return {ta, tb, tc};
}
double len(pt a){
    return pow(pow(a.x, 2)+pow(a.y, 2)+pow(a.z, 2),0.5);
}
double dist(pt x0, pt x1, pt x2){
    double tp = len(cross(sub(x2, x1), sub(x1, x0)));
    double tb = len(sub(x2, x1));
    return  tp/tb;
}
double dot(pt a, pt b){
    return a.x*b.x+a.y*b.y+a.z*b.z;
}
main(){
    int M, N, x, y, z, v, r, D;
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> M;
    bool vis[M];
    vector<pnt> cd;
    vector<pt> wp;
    for (int i = 0; i<M; i++){
        cin >> x >> y >> z >> v >> r;
        cd.pb({x, y, z, v, r});
        vis[i] = false;
    }
    cin >> N;
    wp.pb({0, 0, 0});
    for (int i = 0; i<N; i++){
        cin >> x >> y >> z;
        wp.pb({x, y, z});
    }
    cin >> D;
    double d;
    int ans = 0;
    for (int i = 0; i<N; i++){
        pt x1 = wp[i];
        pt x2 = wp[i+1];
        //cout << "for points: " << x1.x << " " << x1.y << " " << x1.z << " ";
        //cout << x2.x << " " << x2.y << " " << x2.z << "\n";
        for (int j = 0; j<M; j++){
            if (vis[j]) continue;
            pnt x0 = cd[j];
            pt temp = {x0.x, x0.y,x0.z};
            double c1 = dot(sub(temp, x1), sub(x2, x1));
            double c2 = dot(sub(temp, x2), sub(x1, x2));
            //cout << c1 << " " << c2 << "\n";
            if (c1 < 0 || c2 < 0){
                d = min(len(sub(temp, x1)), len(sub(temp, x2)));
            }
            else{
                d = dist(temp, x1, x2);
            }
            //cout << x0.x << " " <<  x0.y << " " << x0.z << " " << d << "\n";
            if (D+x0.r >= d || abs(D+x0.r-d)<0.00001){
                ans += x0.v;
                vis[j] = true;
            }
        }
    }
    cout << ans << "\n";
}
/*
3
2 2 0 1 1
4 2 0 0 0
6 2 0 0 0
1
4 0 0
1
*/