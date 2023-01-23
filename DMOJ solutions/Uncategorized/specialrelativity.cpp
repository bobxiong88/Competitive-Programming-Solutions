#include <bits/stdc++.h>
using namespace std;
#define pdd pair<double, double>
#define mp make_pair
#define pb push_back
vector<pdd> a;
struct psn{
    double px, py, dx, dy;
};
vector<psn> b;
double aqt(double a, double b, double c){
    double delta = sqrt(pow(b, 2)-4*a*c);
    return (-b-delta)/(2*a);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M;
    double C;
    cin >> N >> M >> C;
    for (int i = 0; i<N; i++){
        pdd curr;
        cin >> curr.first >> curr.second;
        a.pb(curr);
    }
    for (int i = 0; i<M; i++){
        psn p;
        cin >> p.px >> p.py >> p.dx >> p.dy;
        b.pb(p);
    }
    double ans = 0;
    for (auto [x, y]: a){
        vector<double> times;
        for (auto [px, py, dx, dy]: b){
            px -= x;
            py -= y;
            times.pb(aqt(pow(dx, 2)+pow(dy, 2)-pow(C, 2), 2*dx*px+2*dy*py, pow(px, 2)+pow(py, 2)));
        }
        sort(times.begin(), times.end());
        double s = 0;
        for (int i = 0; i<M; i++){
            ans += times[i]*i-s;
            s += times[i];
        }
    }
    cout << ans << "\n";
}