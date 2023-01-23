#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>

int main(){
    int N, M, Q, u, v;
    ll a, b, c, d, k;
    cin >> k >> a >> b >> c >> d;
    cin >> N >> M >> Q;
    int T[N*M+1];
    bitset<25000000> pos;
    for (int i = 0; i<N*M+1; i++)
        T[i] = i;
    for (int i = 1; i<N*M+1; i++){
        k = (a*(k*k%d)+b*k%d+c)%d;
        swap(T[i], T[k%i+1]);
    }
    while (Q--){
        cin >> u >> v;
        swap(T[u], T[v]);
    }
    int pnts[N*M+1];
    for (int i = 0; i<N; i++){
        for (int j = 0; j<M; j++){
            pnts[T[i*M+j+1]] = i*M+j;
            pos[i*M+j] = 1;
        }
    }
    for (int v = 1; v<N*M+1; v++){
        int x = pnts[v]/M;
        int y = pnts[v]-x*M;
        if (!pos[x*M+y]) continue;
        cout << v << " ";
        for (int i = x+1; i < N; i++){
            for (int j = y-1; j >= 0; j--){
                if (!pos[i*M+j]) break;
                pos[i*M+j] = 0;
            }
        }
        for (int i = x-1; i >= 0; i--){
            for (int j = y+1; j<M; j++){
                if (!pos[i*M+j]) break;
                pos[i*M+j] = 0;
            }
        }
    }

}