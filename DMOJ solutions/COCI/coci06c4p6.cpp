#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define mx int(2e5)+5
#define inf int(2e9)+10
typedef
tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update>
ost;
pii t[2*mx];
pii porn(pii a, pii b){
    if (a.first > b.first) return a;
    return b;
}
void update(int p, pii v){
    p += mx;
    for (t[p] = porn(t[p], v); p > 1; p >>= 1) t[p >> 1] = porn(t[p], t[p^1]);
}
pii query(int l, int r){
    r++;
    pii res;
    res.first = 0; res.second = 0;
    for (l += mx, r += mx; l < r; l >>= 1, r >>= 1){
        if (l&1) res = porn(res, t[l++]);
        if (r&1) res = porn(res, t[--r]);
    }
    return res;
}
pii aids[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, A, B, x;
    char q;
    cin >> N;
    set<int> lol;
    vector<int> comp;
    vector<pii> tot;
    for (int i = 0; i<N; i++){
        cin >> q;
        if(q == 'D'){
            cin >> A >> B;
            if (!lol.count(B)){
                comp.pb(B);
                lol.insert(B);
            }
            tot.pb(mp(A, B));
        }
        else{
            cin >> x;
            tot.pb(mp(x, 0));
        }
    }
    sort(comp.begin(), comp.end());
    map<int,int> coc;
    for (int i = 0; i<comp.size(); i++){
        coc[comp[i]] = i;
        //cout << comp[i] << " : " << i << "\n";
    }
    ost cum[comp.size()];
    int cnt = 1;
    for (pii q: tot){
        if (!q.second){
            x = q.first;
            auto [A, B] = aids[x];
            // homie in hood?
            int k = cum[B].order_of_key(mp(A, x))+1;
            if (k < cum[B].size()){
                auto it = *cum[B].find_by_order(k);
                cout << it.second << "\n";
                // did not make it out the hood :(
                continue;
            }

            // AIDSSSSSSSSSSSSS
            int l = B+1;
            int r = comp.size()-1;
            int omegalul = inf;
            while (l <= r){
                int m = (l+r)/2;
                pii dmoj = query(B+1, m);
                if (dmoj.first >= A){
                    omegalul = min(omegalul, m);
                    r = m-1;
                }
                else{
                    l = m+1;
                }
            }
            if (omegalul == inf){
                cout << "NE\n";
                continue;
            }
            //cout << "omegalul " << omegalul << "\n";
            k = cum[omegalul].order_of_key(mp(A, -inf));
            auto it = *cum[omegalul].find_by_order(k);
            cout << it.second << "\n";
        }
        else{
            auto [A, B] = q;
            B = coc[B];
            update(B, mp(A, cnt));
            aids[cnt] = mp(A, B);
            cum[B].insert(mp(A, cnt));
            cnt++;
        }
    }
}