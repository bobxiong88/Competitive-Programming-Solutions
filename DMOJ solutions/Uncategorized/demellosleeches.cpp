#include <bits/stdc++.h>
using namespace std;
#define mx 200005
int tree[mx*4][2];
int lazy[mx*4];
int A[mx];
void build(int node, int start, int endd)
{
    if(start == endd)
    {
        tree[node][0] = A[start];
        tree[node][1] = start;
    }
    else
    {
        int mid = (start + endd) / 2;
        build(2*node, start, mid);
        build(2*node+1, mid+1, endd);
        if (tree[2*node][0] < tree[2*node+1][0] ){
            tree[node][0] = tree[2*node][0];
            tree[node][1] = tree[2*node][1];
        }
        else{
            tree[node][0] = tree[2*node+1][0];
            tree[node][1] = tree[2*node+1][1];
        }
    }
}
void lazyUpdate(int node, int start, int endd){
    if(lazy[node] != 0)
    {
        tree[node][0] += lazy[node];
        if(start != endd)
        {
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
void updateRange(int node, int start, int endd, int l, int r, int val)
{
    lazyUpdate(node, start, endd);
    if(start > endd || start > r || endd < l)
        return;
    if(start >= l && endd <= r)
    {
        tree[node][0] += val;
        if(start != endd)
        {
            lazy[node*2] += val;
            lazy[node*2+1] += val;
        }
        return;
    }
    int mid = (start + endd) / 2;
    updateRange(node*2, start, mid, l, r, val);
    updateRange(node*2 + 1, mid + 1, endd, l, r, val);
    if (tree[2*node][0] < tree[2*node+1][0] ){
        tree[node][0] = tree[2*node][0];
        tree[node][1] = tree[2*node][1];
    }
    else{
        tree[node][0] = tree[2*node+1][0];
        tree[node][1] = tree[2*node+1][1];
    }
}

pair<int, int> queryRange(int node, int start, int endd, int l, int r)
{
    if(start > endd || start > r || endd < l)
        return make_pair(mx, mx);
    lazyUpdate(node, start, endd);
    if(start >= l && endd <= r)
        return make_pair(tree[node][0], tree[node][1]);
    int mid = (start + endd) / 2;
    auto[v1, x1] = queryRange(node*2, start, mid, l, r);
    auto[v2, x2] = queryRange(node*2 + 1, mid + 1, endd, l, r);
    if (v1 < v2){
        return make_pair(v1, x1);
    }
    else{
        return make_pair(v2, x2);
    }
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    for (int i = 0; i< 4*mx; i++){
        tree[i][0] = 1e6;
    }
    int N, Q, l, r, x, v, idx;
    cin >> N;
    for(int i = 1; i<=N; i++)
        cin >> A[i];
    cin >> Q;
    build(1, 1, N);
    for(int i = 0; i<Q; i++){
        cin >> l >> r;
        updateRange(1, 1, N, l, r, -1);
        tie(v, idx) = queryRange(1, 1, N, l, r);
        x = 0;
        while (v < 0){
            updateRange(1, 1, N, idx, idx, 1e6);
            tie(v, idx) = queryRange(1, 1, N, l ,r);
            x++;
        }
        cout << x << "\n";
    }
    return 0;
}