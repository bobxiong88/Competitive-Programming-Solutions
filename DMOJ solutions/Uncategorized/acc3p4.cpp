// credit goes to: https://codeforces.com/blog/entry/44478?#comment-290057

#include <bits/stdc++.h>
using namespace std;
#define mx 1000005
struct node{
    int sum, la, lb;
};
vector<node> t(4*mx);
int a[mx];
node poo;
void lazyUpdate(int n, int l, int r){
    if (t[n].la){
        t[n].sum += (r-l+1)*t[n].la;
        if (l != r){
            t[2*n].la += t[n].la;
            t[2*n+1].la += t[n].la;
        }
        t[n].la = 0;
    }
    if (t[n].lb){
        int mid = (l+r)/2;
        t[n].sum += ((r-l+1)*(r-l+1)/2)*t[n].lb;
        if (l != r){
            t[2*n].lb += t[n].lb;
            t[2*n+1].lb += t[n].lb;
            t[2*n+1].la += t[n].lb*(mid-l+1);
        }
        t[n].lb = 0;
    }
}
node comb(node a, node b){
    node temp;
    temp.sum = a.sum+b.sum;
    temp.la = 0;
    temp.lb = 0;
    return temp;
}
void build(int n, int l, int r){
    if (l == r){
        t[n].sum = a[l];
        return;
    }
    int mid = (l+r)/2;
    build(n*2, l, mid);
    build(n*2+1,mid+1,r);
    t[n] = comb(t[2*n],t[2*n+1]);
}
void update(int n, int l, int r, int a, int b, int v, int start){
    lazyUpdate(n, l, r);
    if (l > r || l > b || a > r) return;
    if (a <= l && r <= b){
        t[n].la += start+v+(l-a)*v;
        t[n].lb += v;
        lazyUpdate(n, l, r);
        return;
    }
    int mid = (l+r)/2;
    update(n*2, l, mid, a, b, v,start);
    update(n*2+1,mid+1,r,a,b, v,start);
    t[n] = comb(t[2*n],t[2*n+1]);
}
node query(int n, int l, int r, int a, int b){
    lazyUpdate(n, l, r);
    if (l > r || l > b || a > r) return {0,0,0};
    if (a <= l && r <= b) return t[n];
    int mid = (l+r)/2;
    return comb(query(n*2, l, mid, a, b), query(n*2+1,mid+1,r,a,b));
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, Q, a, b, v, monkey, start;
    cin >> N >> Q;
    while (Q--){
        cin >> monkey;
        if (monkey == 1){
            cin >> a >> b >> v;
            update(1, 1, N, a, b, v, 0);
            //for (int i = 1; i<=N; i++) cout << query(1,1,N,i,i).sum << " ";
            //cout << "\n";
        }
        else{
            cin >> a >> b;
            cout << query(1, 1, N, a, b).sum << "\n";
        }
    }
}