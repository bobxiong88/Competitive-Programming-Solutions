#include <bits/stdc++.h>
using namespace std;
using ld = long double;
#define double ld
#define mx int(1e4)+5
#define pb push_back
#define mp make_pair
#define inf double(2e10)
double a[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, k;
    cin >> N >> k;
    for (int i = 1; i<=N; i++){
        cin >> a[i];
    }
    vector<double> t0, t1, t2;
    t0.pb(0);
    t1.pb(a[1]);
    t2.pb(a[1]+a[2]-min(a[1],a[2])/2);
    t2.pb(a[1]+a[2]);
    for (int i = 3; i <= N; i++){
        double one, two, tre;
        vector<double> nw,ti;
        one = a[i];
        two = a[i]+a[i-1]-min(a[i],a[i-1])/2;
        tre = a[i]+a[i-1]+a[i-2]-min(min(a[i], a[i-1]), a[i-2]);
        int x, y, z;
        x = 0;
        y = 0;
        z = 0;
        while (ti.size()<k){
            double xi, yi, zi;
            if (x >= t0.size()) xi = inf;
            else{xi = t0[x]+tre;}
            if (y >= t1.size()) yi = inf;
            else{yi = t1[y]+two;}
            if (z >= t2.size()) zi = inf;
            else{zi = t2[z]+one;}
            double nxt = min(xi, min(yi, zi));
            if (nxt == xi){
                x++;
            }
            if (nxt == yi){
                y++;
            }
            if (nxt == zi){
                z++;
            }
            if (nxt == inf){
                break;
            }
            ti.pb(nxt);
        }
        t0.assign(t1.begin(), t1.end());
        t1.assign(t2.begin(), t2.end());
        t2.assign(ti.begin(), ti.end());
        //for (auto x: t0) cout << x << " "; cout << "\n";
        //for (auto x: t1) cout << x << " "; cout << "\n";
        //for (auto x: t2) cout << x << " "; cout << "\n";
    }
    cout << std::setprecision(1) << fixed;
    if (t2.size()>=k) cout << t2[k-1] << "\n";
    else cout << "-1" << "\n";
}