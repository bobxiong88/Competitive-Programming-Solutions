#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N;
    cin >> N;
    long long ans = 0;
    int prev = 0;
    int curr = 0;
    for (int i = 0; i<N; i++){
        cin >> curr;
        if (i){
            ans += max(curr, prev);
        }
        prev = curr;
    }
    cout << ans << "\n";
}