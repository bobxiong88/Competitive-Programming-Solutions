#include <bits/stdc++.h>
using namespace std;
#define mx 250001
struct sad{
    int poo[10];
};
int temp[10];
sad t[4*mx];
int lazy[mx*4], a[mx];
void build(int node, int tl, int tr){
    if (tl == tr){
        t[node].poo[a[tl]]++;
    }
    else{
        int mid = (tl+tr)/2;
        build(node*2, tl, mid);
        build(node*2+1, mid+1, tr);
        for (int i = 0; i<10; i++){
            t[node].poo[i] = t[node*2].poo[i] + t[node*2+1].poo[i];
        }
    }
}
void update(int node, int v){
    int temp[10];
    for (int i = 0; i<10; i++){
        temp[(i+v)%10] = t[node].poo[i];
    }
    for (int i = 0; i<10; i++){
        t[node].poo[i] = temp[i];
    }
}
void lazyUpdate(int node, int tl, int tr){
    if (lazy[node] != 0){
        update(node, lazy[node]);
        if (tl != tr){
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
void update(int node, int tl, int tr, int l, int r){
    lazyUpdate(node, tl, tr);
    if (tl > r || l > tr) return;
    if (l <= tl && tr <= r){
        update(node, 1);
        if (tl != tr){
            lazy[node*2] += 1;
            lazy[node*2+1] += 1;
        }
        return;
    }
    int mid = (tl+tr)/2;
    update(node*2, tl, mid, l, r);
    update(node*2+1, mid+1, tr, l, r);
    for (int i = 0; i<10; i++){
        t[node].poo[i] = t[node*2].poo[i]+t[node*2+1].poo[i];
    }
}
sad query(int node, int tl, int tr, int l, int r){
    lazyUpdate(node, tl, tr);
    sad res;
    if (tl > r || l > tr) return res;
    if (l <= tl && tr <= r) return t[node];
    int mid = (tl + tr)/2;
    sad left = query(node*2, tl, mid, l, r);
    sad right = query(node*2+1, mid+1, tr, l, r);
    for (int i = 0; i<10; i++){
        res.poo[i] = left.poo[i]+right.poo[i];
    }
    return res;
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M, l, r;
    string S;
    cin >> N >> M;
    cin >> S;
    for (int i = 0; i<N; i++) a[i+1] = (int)S[i]-48;
    build(1, 1, N);
    while(M--){
        cin >> l >> r;
        sad res = query(1, 1, N, l, r);
        int ans = 0;
        for (int i = 0; i<10; i++) ans += res.poo[i]*i;
        cout << ans << "\n";
        update(1, 1, N, l, r);
    }
}