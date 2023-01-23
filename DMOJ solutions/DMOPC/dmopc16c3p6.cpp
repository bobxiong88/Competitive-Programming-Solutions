#include <iostream>
#include <vector>
#define pb push_back
#define f first
#define s second
#define mp make_pair
using namespace std;
const int inf = 2147483647;
const int mx = int(1e5)+1;
int N, Q, x, y, tsum, tpre, tsuf;
char q;
struct porn{
    porn *lt, *rt;
    int sum, pre, suf;
    porn(porn *lt, porn *rt, int x) : lt(lt), rt(rt), sum(x){
        pre = sum;
        suf = sum;
        if (lt&&rt){
            sum = lt->sum+rt->sum;
            pre = max(lt->pre, lt->sum+rt->pre);
            suf = max(rt->suf, lt->suf+rt->sum);
        }
    }
};
#define pr pair<porn*, bool>
porn* build(int tl, int tr){
    if (tl == tr) {
            cin >> x;
            return new porn(0, 0, x);
    }
    int tm = (tl+tr)/2;
    return new porn(build(tl, tm), build(tm+1, tr), 0);
}
porn* update(porn *node, int tl, int tr, int p, int v){
    if (tl == tr) return new porn(0, 0,  v);
    int tm = (tl+tr)/2;
    if (p <= tm) return new porn(update(node->lt, tl, tm, p, v), node->rt, 0);
    else return new porn(node->lt, update(node->rt, tm+1, tr, p, v), 0);
}
pr query(porn *node, int tl, int tr, int l, int r){
    if (l <= tl && tr <= r) return mp(node, false);
    int tm = (tl+tr)/2;
    if (l > tm) return query(node->rt, tm+1, tr, l, r);
    if (r <= tm) return query(node->lt, tl, tm, l, r);
    pr left = query(node->lt, tl, tm, l, r);
    pr rght = query(node->rt, tm+1, tr, l, r);
    porn* res = new porn(0, 0, 0);
    if (left.f->sum != -inf) res->sum += left.f->sum;
    if (rght.f->sum != -inf) res->sum += rght.f->sum;
    res->pre = max(left.f->pre, left.f->sum+rght.f->pre);
    res->suf = max(rght.f->suf, rght.f->sum+left.f->suf);
    if (left.s) delete left.f;
    if (rght.s) delete rght.f;
    return mp(res, true);
}
vector<porn*>roots;
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin >> N;
    roots.pb(build(1, N));
    cin >> Q;
    while (Q--){
        cin >> q;
        if (q == 'U'){
            cin >> x >> y;
            roots.pb(update(roots.back(), 1, N, x, y));
        }
        else if (q == 'G'){
            cin >> x;
            roots.pb(roots[x]);
        }
        else{
            cin >> x >> y;
            pr res = query(roots.back(), 1, N, x, y);
            if (q == 'P') cout << res.f->pre << "\n";
            else cout << res.f->suf << "\n";
            if (res.s) delete res.f;
        }
    }
}
/*
5
-1 1 1 1 9
10
P 1 1
*/