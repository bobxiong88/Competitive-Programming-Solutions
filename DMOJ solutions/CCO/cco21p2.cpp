#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define inf int(4e18)
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int K, Q, D, M, n, x, curr;
    cin >> K >> Q >> D >> M;
    vector<int> d;
    for (int i = 0; i<D; i++){
        cin >> x;
        d.pb(x);
    }
    sort(d.begin(), d.end(), greater<>());
    while (Q--){
        unordered_set<int> vis;
        unordered_map<int,pii> par;
        cin >> n;
        queue<int> que;
        que.push(n);
        bool found = false;
        int cnt = 0;
        par[n] = mp(n, -inf);
        while (!que.empty()){
            curr = que.front(); que.pop();
            if (curr > inf) continue;
            if (curr==0&&cnt){
                found = true;
                break;
            }
            cnt++;
            for (int k: d){
                if ((curr-k)%K == 0 && !vis.count((curr-k)/K) && curr-k < inf){
                    que.push((curr-k)/K);
                    par[(curr-k)/K] = mp(curr, k);
                    vis.insert((curr-k)/K);
                }
            }
        }
        if (found){
            while (true){
                cout << par[curr].second;
                par[curr].second = -inf ;
                curr = par[curr].first;
                if (curr != n) cout << " ";
                else break;
            }
        }
        else{
            cout << "IMPOSSIBLE";
        }
        cout << "\n";
    }
}