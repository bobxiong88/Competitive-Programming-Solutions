#include <bits/stdc++.h>
using namespace std;
#define mx 505
#define pb push_back
#define pdd pair<double, double>
#define mp make_pair
const double inf = 1e9;
const double pi = 3.14159265358979323846264338327950288419716939937510;
//const double error = 0.000001;
struct line{
    double left, right, m, b;
};
struct disk{
    double a, r;
};
int n, cnt;
double a, ht;
double r[mx], h[mx];
vector<line> lines;
vector<disk> disks;
double f(double x){
    double ans = 0;
    for (auto[left, right, m, b]: lines){
        if (left <= x && x <= right){
            ans = max(ans, m*x+b);
        }
    }
    for (auto[a, r]:disks){
        if (a-r <= x && x <= a+r){
            double k = r*r;
            double t = (x-a)*(x-a);
            if (k < t) continue;
            ans = max(ans, sqrt(k-t));
        }
    }
    return ans;
}
double S(double left, double right){
    return (right-left)*(f(left)+4*f((left+right)/2)+f(right))/6;
}
/*
double solve(double left, double right, double res){
    double mid = (left+right)/2;
    double sleft = simp(left, mid);
    double sright = simp(mid, right);
    if (abs(sleft+sright-res)<error){
        return sleft+sright;
    }
    return solve(left, mid, sleft)+solve(mid, right, sright);
}
*/
double asr(double a, double b, double e){
    double m = (a+b)/2;
    double Sam = S(a, m);
    double Smb = S(m, b);
    double Sab = S(a, b);
    cnt++;
    if (abs(Sam+Smb-Sab)/15 < e)
        return Sam+Smb;
    else
        return asr(a, m, e/2) + asr(m, b, e/2);
}
double speed(double a, double b, double Sab, double e){
    double m = (a+b)/2;
    double Sam = S(a, m);
    double Smb = S(m, b);
    if (abs(Sam+Smb-Sab)/15 < e)
        return Sam+Smb;
    else
        return speed(a, m, Sam, e/2) + speed(m, b, Smb, e/2);
}
pdd quad(double a, double b, double c){
    double delta = pow(b, 2)-4*a*c;
    if (abs(delta) <= 0.001) delta = 0;
    if (delta<0) return mp(inf, inf);
    double r1 = (-b-sqrt(delta))/(2*a);
    double r2 = (-b+sqrt(delta))/(2*a);
    return mp(r1, r2);
}
int main(){
    //freopen("bad.txt", "r", stdin);
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> n >> a;
    for (int i = 0; i<=n; i++){
        cin >> h[i];
        ht += h[i];
    }
    for (int i = 0; i<n; i++){
        cin >> r[i];
    }
    disks.pb({-ht/tan(a), 0});
    for (int i = 0; i<n; i++){
        ht -= h[n-i];
        double x = -ht/tan(a);
        disks.pb({x, r[n-i-1]});
        auto [xA, rA] = disks[disks.size()-2];
        auto [xB, rB] = disks[disks.size()-1];
        double d = xB-xA;
        if (abs(rB-rA) >= d) continue;
        double beta = asin((rB-rA)/d);
        double m = tan(beta);
        double theta = pi/2-beta;
        double x1 = xA-rA*cos(theta);
        double x2 = xB-rB*cos(theta);
        double y1 = rA*sin(theta);
        double b = y1-m*x1;
        lines.pb({x1, x2, m, b});
        //cout << "y = " << m << "x+"<<k<<"\n";
    }
    double left = 1e9;
    double right = -1e9;
    vector<pdd> range;
    for (auto[a,r]:disks){
        left = min(left, a-r);
        right = max(right, a+r);
        //cout << "y^2 = "<<r<<"^2-(x-"<<a<<")^2"<<"\n";
    }
    vector<double> disc;
    for (int i = 0; i<(int)disks.size(); i++){
        auto [xA, rA] = disks[i];
        for (int j = i+1; j<(int)disks.size(); j++){
            auto [xB, rB] = disks[j];
            if (xA==xB) continue;
            double x = ((pow(rA, 2)-pow(rB, 2))/(xB-xA)+(xA-xB))/2;
            if (xA-rA <= x && xB-rB <= x && xA+rA >= x && xB+rB >= x) disc.pb(x);
        }
        for (int j = 0; j<(int)lines.size(); j++){
            auto [x1, x2, m, b] = lines[j];
            auto [r1, r2] = quad(pow(m,2) + 1, 2*m*b - 2*xA,pow(b, 2) + pow(xA, 2) - pow(rA, 2));
            if (r1==inf) continue;
            x1 -= 0.001;
            x2 += 0.001;
            if (x1 <= r1 && r1 <= x2 && xA-rA <= r1 && r1 <= xA+rA) disc.pb(r1);
            if (x1 <= r2 && r2 <= x2 && xA-rA <= r2 && r2 <= xA+rA) disc.pb(r2);
        }
    }
    for (int i = 0; i<(int)lines.size(); i++){
        auto [x1A, x2A, mA, bA] = lines[i];
        for (int j = i+1; j<(int)lines.size(); j++){
            auto [x1B, x2B, mB, bB] = lines[j];
            if (lines[i].m == lines[j].m) continue;
            double x = (bA-bB)/(mB-mA);
            if (x1A <= x && x <= x2A && x1B <= x && x <= x2B) disc.pb(x);
        }
    }
    disc.pb(left);
    disc.pb(right);
    sort(disc.begin(), disc.end());
    double ans = 0;
    double e = 0.0000001;
    //cout << "x = " << disc[0] << "\n";
    for (int i = 0; i<(int)disc.size()-1; i++){
        //cout << "x = " << disc[i+1] << "\n";
        if (disc[i]==disc[i+1]) continue;
        ans += asr(disc[i], disc[i+1], e);
        //ans += speed(disc[i], disc[i+1], S(disc[i], disc[i+1]), e*(disc[i+1]-disc[i])/(right-left));
    }

    cout << fixed << setprecision(2);
    cout << ans*2 << "\n";
    //cout << disc.size() << " " << cnt << "\n";
}