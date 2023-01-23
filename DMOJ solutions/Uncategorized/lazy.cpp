#include <bits/stdc++.h>
//#pragma GCC optimize("Ofast")
using namespace std;
// used code from hackerearth.com
using ll = long long;
#define int ll
int MAXN = 1000000000000;
int tree[400004] = {0};
int lazy[400004][2];
int A[100001] = {0};
void lazyUpdate(int node, int start, int endd){
    if(lazy[node][0] != 0 || lazy[node][1] != 0)
    {
        if (lazy[node][0] != 0) tree[node] = lazy[node][0];
        tree[node] += lazy[node][1];
        if(start != endd)
        {
            lazy[node*2][1] += lazy[node][1];
            lazy[node*2+1][1] += lazy[node][1];
            if (lazy[node][0] != 0){
                lazy[node*2][0] = lazy[node][0];
                lazy[node*2][1] = lazy[node][1];
                lazy[node*2+1][0] = lazy[node][0];
                lazy[node*2+1][1] = lazy[node][1];
            }

        }
        lazy[node][0] = 0;
        lazy[node][1] = 0;
    }
}
void build(int node, int start, int endd)
{
    if(start == endd)
    {
        tree[node] = A[start];
    }
    else
    {
        int mid = (start + endd) / 2;
        build(2*node, start, mid);
        build(2*node+1, mid+1, endd);
        tree[node] = min(tree[2*node], tree[2*node+1]);
    }
}
void updateRange(int node, int start, int endd, int l, int r, int val)
{
    lazyUpdate(node, start, endd);
    if(start > endd || start > r || endd < l)
        return;
    if(start >= l && endd <= r)
    {
        // Segment is fully within range
        tree[node] += val;
        if(start != endd)
        {
            // Not leaf node
            lazy[node*2][1] += val;
            lazy[node*2+1][1] += val;
        }
        return;
    }
    int mid = (start + endd) / 2;
    updateRange(node*2, start, mid, l, r, val);
    updateRange(node*2 + 1, mid + 1, endd, l, r, val);
    tree[node] = min(tree[node*2], tree[node*2+1]);
}
void u2(int node, int start, int endd, int l, int r, int val)
{
    lazyUpdate(node, start, endd);
    if(start > endd || start > r || endd < l)
        return;
    if(start >= l && endd <= r)
    {
        // Segment is fully within range
        tree[node] = val;
        if(start != endd)
        {
            // Not leaf node
            lazy[node*2][0] = val;
            lazy[node*2][1] = 0;
            lazy[node*2+1][0] = val;
            lazy[node*2+1][1] = 0;
        }
        return;
    }
    int mid = (start + endd) / 2;
    u2(node*2, start, mid, l, r, val);
    u2(node*2 + 1, mid + 1, endd, l, r, val);
    tree[node] = min(tree[node*2], tree[node*2+1]);
}
int queryRange(int node, int start, int endd, int l, int r)
{
    if(start > endd || start > r || endd < l)
        return MAXN;
    lazyUpdate(node, start, endd);
    if(start >= l && endd <= r)
        return tree[node];
    int mid = (start + endd) / 2;
    int p1 = queryRange(node*2, start, mid, l, r);
    int p2 = queryRange(node*2 + 1, mid + 1, endd, l, r);
    return min(p1, p2);
}
main(){
    cin.tie(0); cin.sync_with_stdio(0);
    cout.tie(0);
    int N, Q, q, l, r, v;
    cin >> N >> Q;
    for(int i = 1; i<(N+1)*4; i++){
        tree[i] = MAXN;
    }
    for(int i = 1; i<=N; i++) cin >> A[i];
    build(1, 1, N);
    for(int i = 0; i<Q; i++){
        cin >> q;
        if(q == 1){
            cin >> l >> r >> v;
            updateRange(1, 1, N, l, r, v);
        }
        else if(q == 2){
            cin >> l >> r >> v;
            u2(1, 1, N, l, r, v);
        }
        else{
            cin >> l >> r;
            cout << queryRange(1, 1, N, l, r) << "\n";
        }
    }
}
/*
5 20
1 2 3 4 5
3 2 4
2 1 4 1
3 1 1
3 2 2
3 2 3
3 1 2
3 3 3
3 3 4
3 4 5
*/