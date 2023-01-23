#include <bits/stdc++.h>
using namespace std;
#define mx int(1e7)+5
int sieve[mx];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int A, B;
    cin >> A >> B;
    long long ans = 0;
    for (int i = 1; i<=B; i++){
        for (int j = 2*i; j <= B; j+= i){
            sieve[j] += i;
        }
        if (i >= A) ans += abs(i-sieve[i]);
    }
    cout << ans << "\n";
}