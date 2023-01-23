#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define mx 2000
struct plane{
    double m, b;
    int c;
};
int X, K, N, Q, C;
double x, A, B;
vector <plane> f;
int t[mx][2*mx];
vector <vector<pair<double, int>>> arr(mx);
vector <vector<pair<double, int>>> pro(mx);
int sum[mx] = {0};
void build(int i, int n){
    for (int j = n-1; j>0; --j) t[i][j] = max(t[i][j<<1],t[i][j<<1|1]);
}
int query(int i, int n, int l, int r){
    r ++;
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = max(t[i][l++], res);
        if (r&1) res = max(t[i][--r], res);
    }
    return res;
}
int sleft(int i, int v){
    int l = 0;
    int r = pro[i].size()-1;
    if (v <= pro[i][l].first){
        return l;
    }
    if (v >= pro[i][r].first){
        return r;
    }
    while (l <= r){
        int m = floor((l+r)/2);
        if (pro[i][m].first<=v && v<pro[i][m+1].first){
            return m;
        }
        else if(pro[i][m].first > v){
            r = m-1;
        }
        else {
            l = m+1;
        }
    }
}
int sright(int i, int v){
    int l = 0;
    int r = pro[i].size()-1;
    if (v <= pro[i][l].first){
        return 0;
    }
    if (v >= pro[i][r].first){
        return r;
    }
    while (l <= r){
        int m = floor((l+r)/2);
        if (pro[i][m].first<v && v<=pro[i][m+1].first){
            return m;
        }
        else if(pro[i][m].first == v){
            return m-1;
        }
        else if(pro[i][m].first > v){
            r = m-1;
        }
        else {
            l = m+1;
        }
    }
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int factor = int(1e6);
    cin >> X >> K >> N >> Q;
    for (int i = 0; i<N; i++){
        cin >> A >> B >> C;
        A*=factor; B*=factor;
        double m = (B-A)/X;
        double b = A;
        f.push_back({m, b, C});
    }
    for (int i = 0; i<N; i++){
        int sum = 0;
        for (int j = 0; j<N; j++){
            if (i != j){
                if (f[i].m != f[j].m){
                    x = (f[j].b-f[i].b)/(f[i].m-f[j].m);
                    if (x <= 0){
                        if (f[j].m > f[i].m)
                            sum += f[j].c;
                    }
                    else if (f[j].m > f[i].m){
                        if (x < X){
                            arr[i].push_back({x, f[j].c});
                        }
                    }
                    else{
                        if (x < X){
                            arr[i].push_back({x, -f[j].c});
                        }
                        sum += f[j].c;
                    }
                }
                else {
                    if (f[j].b > f[i].b){
                        sum += f[j].c;
                    }
                }
            }
        }
        arr[i].push_back(make_pair(0, sum));
    }
    for(int i = 0; i<N; i++){
        sort(arr[i].begin(), arr[i].end());
        int v = 0;
        for (int j = 0; j<arr[i].size(); j++){
            v += arr[i][j].second;
            if (abs(arr[i][j+1].first-arr[i][j].first)>0.0000000000001){
                pro[i].push_back(make_pair(arr[i][j].first, v));
            }
        }
        int n = pro[i].size();
        for(int j = 0; j<n; j++){
            t[i][n+j] = pro[i][j].second;
        }
        build(i, n);
    }
    while (Q--){
        int P, S;
        cin >> P >> S;
        P--;
        int l = sleft(P, S);
        int r = sright(P, S+K);
        cout << query(P, pro[P].size(), l, r) << "\n";
    }
}