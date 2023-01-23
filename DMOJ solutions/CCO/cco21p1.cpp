#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define mx int(1e5)+5
int bit[mx];
vector<int> loc[mx];
int c[mx];
map<pii,int> cache;
int lsb(int x){
    return x&(-x);
}
int query(int x){
    int res = 0;
    for (int i = x; i>0; i-=lsb(i))
        res += bit[i];
    return res;
}
void update(int x, int v){
    for (int i = x; i<mx; i+=lsb(i))
        bit[i] += v;
}
int qa(int l, int r){
    return query(r)-query(l-1);
}
int f(int x, int y){
    if (cache.count(mp(x, y))) return cache[mp(x, y)];
    int res = 0;
    int cnt = 0;
    for (int j = 0; j<loc[y].size(); j++){
        int l = 0;
        int r = loc[x].size()-1;
        if (loc[x][l] > loc[y][j]){
            cnt = 0;
            l = r+1;
        }
        if (loc[x][r] < loc[y][j]){
            cnt = loc[x].size();
            l = r+1;
        }
        while (l <= r){
            int m = (l+r)/2;
            if (loc[x][m-1] < loc[y][j] && loc[y][j] < loc[x][m]){
                cnt = m;
                break;
            }
            if (loc[x][m] < loc[y][j])
                l = m+1;
            else
                r = m-1;
        }
        res += cnt;
    }
    cache[mp(x,y)] = res;
    return res;
}
/*
int f(int x, int y){
    int res = 0;
    int i = 0;
    int j = 0;
    for (int j = 0; j<loc[y].size(); j++){
        while (i < loc[x].size() && loc[x][i] < loc[y][j]) i++;
        res += i;
    }
    return res;
}
*/
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, K, Q, ans, x, y, j, inc;
    cin >> N >> K >> Q;
    ans = 0;
    int tar[K+1];
    int a[N+1];
    for (int i = 1; i<=N; i++){
        cin >> a[i];
        ans += qa(a[i]+1, N);
        update(a[i], 1);
        loc[a[i]].pb(i);
        c[a[i]]++;
    }
    for (int i = 0; i<=K; i++) tar[i] = i;
    while (Q--){
        cin >> j;
        x = tar[j];
        y = tar[j+1];
        swap(tar[j], tar[j+1]);
        //ans += f(x, y)- f(y,x);
        if (loc[x].size() < loc[y].size()) inc = c[x]*c[y]-2*f(y, x);
        else inc = 2*f(x,y)-c[x]*c[y];
        ans += inc;
        cout << ans << "\n";
    }
}