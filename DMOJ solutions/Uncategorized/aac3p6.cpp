#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int R, C, N, M, x, D;
    vector<int> a, b;
    cin >> R >> C;
    cin >> N >> M;
    bool inv = false;
    if (R > C){
        for (int i = 0; i<N; i++){
            cin >> x;
            b.pb(x);
        }
        for (int i = 0; i<M; i++){
            cin >> x;
            a.pb(x);
        }
        swap(R, C); swap(N, M); inv = true;
    }
    else{
        for (int i = 0; i<N; i++){
            cin >> x;
            a.pb(x);
        }
        for (int i = 0; i<M; i++){
            cin >> x;
            b.pb(x);
        }
    }
    D = C-R;
    //N+=1;
    assert(a.size()==N&&b.size()==M);
    deque<int> curr;
    int j = 0;
    bool pos = true;
    vector<int> ans;
    for (int i: b){
        while (j < a.size() && a[j] <= i){
            curr.pb(a[j]);
            j++;
        }
        while (!curr.empty() && curr[0] < i-D){
            curr.pop_front();
        }
        if (curr.size() == D+1){
            pos = false;
            break;
        }
        if (!curr.empty()){
            int l = 0;
            int r = curr.size()-1;
            if (curr[0] != i-D){
                ans.pb(D);
                continue;
            }
            if (curr.back() < i){
                ans.pb(0);
                continue;
            }
            while (l < r){
                int m = (l+r)/2;
                if (curr[m]- curr[0] == m) l = m+1;
                else r = m;
            }
            ans.pb(i-curr[r]+1);
        }
        else{
            ans.pb(0);
        }
    }
    if (pos){
        cout << C+1 << "\n";
        if (inv){
            for (int i = 0; i<ans.size(); i++){
                cout << ans[i];
                if (i != ans.size()-1) cout << " ";
            } cout << "\n";
            for (int i = 0; i<N; i++) {
                cout << 0;
                if (i != N-1) cout << " ";
            }cout << "\n";
        }
        else{
            for (int i = 0; i<N; i++) {
                cout << 0;
                if (i != N-1) cout << " ";
            }cout << "\n";
            for (int i = 0; i<ans.size(); i++){
                cout << ans[i];
                if (i != ans.size()-1) cout << " ";
            } cout << "\n";
        }
    }
    else{
        cout << max(R+1, C+1)+1 << "\n";
        if (inv){
            for (int i = 0; i<M; i++) {cout << (b[i]+1)%2 ; if (i != M-1) cout << " ";} cout << "\n";
            for (int i = 0; i<N; i++) {cout << a[i]%2 ; if (i != N-1) cout << " ";} cout << "\n";
        }
        else{
            for (int i = 0; i<N; i++) {cout << a[i]%2 ; if (i != N-1) cout << " ";} cout << "\n";
            for (int i = 0; i<M; i++) {cout << (b[i]+1)%2 ; if (i != M-1) cout << " ";} cout << "\n";
        }
    }

}