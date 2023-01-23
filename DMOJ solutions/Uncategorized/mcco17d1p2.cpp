#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define int ll
//used template lazy propagation from hackerrank.com
int tree[800004] = {0};
int lazy[800004] = {0};
int arr[200001] = {0};
void lazyUpdate(int node, int start, int endd){
    if(lazy[node] != 0)
    {
        tree[node] += lazy[node];
        if(start != endd)
        {
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
void build(int node, int start, int endd)
{
    if(start == endd)
    {
        tree[node] = arr[start];
    }
    else
    {
        int mid = (start + endd) / 2;
        build(2*node, start, mid);
        build(2*node+1, mid+1, endd);
        tree[node] = max(tree[2*node], tree[2*node+1]);
    }
}
void updateRange(int node, int start, int endd, int l, int r, int val)
{
    lazyUpdate(node, start, endd);
    if(start > endd || start > r || endd < l)
        return;
    if(start >= l && endd <= r)
    {
        tree[node] += val;
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
    tree[node] = max(tree[node*2], tree[node*2+1]);
}
int queryRange(int node, int start, int endd, int l, int r)
{
    if(start > endd || start > r || endd < l)
        return -1;
    lazyUpdate(node, start, endd);
    if(start >= l && endd <= r)
        return tree[node];
    int mid = (start + endd) / 2;
    int p1 = queryRange(node*2, start, mid, l, r);
    int p2 = queryRange(node*2 + 1, mid + 1, endd, l, r);
    return max(p1, p2);
}
int n, k, Q, q, p, l, r, v;
main(){
    cin.tie(0); cin.sync_with_stdio(0);
    cin >> n >> k >> Q;
    build(1, 1, n);
    while (Q--){
        cin >> q;
        if (!q){
            cin >> p >> v;
            p++;
            updateRange(1, 1, n, max(ll(1), p-k+1), p, v);
        }
        else{
            cin >> l >> r;
            l++; r++;
            cout << queryRange(1, 1, n, l, r) << "\n";
        }
    }
}