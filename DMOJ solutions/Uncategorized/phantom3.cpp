#include <bits/stdc++.h>
#include <bitset>
using namespace std;
using ll = long long;

bool prime(ll N){
    if(N == 1)
        return false;
    if(N == 2)
        return true;
    for(ll i = 2; i<=sqrt(N)+1; i++){
        if(N%i==0)
            return false;
    }
    return true;
}
bitset<int(3e7)> sieve;
int main(){
    //algorithm from cp-algorithms.com
    ll N, M;
    cin >> N >> M;
    if(prime(N))
        N--;
    M--;
    ll lim = sqrt(M)+1;
    vector<bool> mark(lim+1, false);
    vector<ll> primes;
    for(ll i = 2; i<= lim; ++i){
        if(!mark[i]){
            primes.emplace_back(i);
            for(ll j = i*i; j<=lim; j+=i)
                mark[j] = true;
        }
    }

    for (ll i: primes){
        for(ll j = max(i*i, (N+i-1)/i*i); j <= M; j+=i)
            sieve.set(j-N);
    }
    int c = 0;
    for(int i = 0; i<int(M-N); i++){
        if(!sieve.test(i+1)){
            //cout << i+N << "\n";
            c+=1;
        }
    }
    cout << c;

}