#include <bits/stdc++.h>
using namespace std;
int ans = 1000000000;
int n;
vector<int>a;
void solve(vector<int> a, vector<int> curr){
    if (curr.size() == n){
        int s = 0;
        for (int i = 0; i<n; i++) s += curr[i];
        ans = min(ans,s);
        int gay = 0;
        for (int i = 0; i<n ;i++){
            s-=curr[i];
            gay+=curr[i];
            ans = min(ans,abs(s-gay));
        }
        return;
    }
    for (int i = 0; i<a.size(); i++){
        int c = a[i];
        a.erase(a.begin()+i);
        curr.push_back(c);
        solve(a, curr);
        a.push_back(c);
        curr.erase(curr.begin()+curr.size()-1);
    }
}
int main(){
    cin >> n;
    for (int i = 0; i<n; i++){
        int c;
        cin >> c;
        a.push_back(c);
    }
    vector<int> curr;
    solve(a, curr);
    cout << ans;
}