#include <bits/stdc++.h>
using namespace std;
#define mx 1000005
int tree[mx*4];
int lazy[mx*4];
int A[mx], L;
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
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}
void lazyUpdate(int node, int start, int endd){
    if(lazy[node] != 0)
    {
        if (lazy[node]%2) tree[node] = (endd - start + 1)-tree[node];
        if(start != endd)
        {
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
void update(int node, int start, int endd, int l, int r)
{
    lazyUpdate(node, start, endd);
    if(start > endd || start > r || endd < l)
        return;
    if(start >= l && endd <= r)
    {
        tree[node] = (endd - start + 1)-tree[node];
        if(start != endd)
        {
            lazy[node*2] += 1;
            lazy[node*2+1] += 1;
        }
        return;
    }
    int mid = (start + endd) / 2;
    update(node*2, start, mid, l, r);
    update(node*2 + 1, mid + 1, endd, l, r);
    tree[node] = tree[node*2] + tree[node*2+1];
}
int query(int node, int tl, int tr, int v){
    	lazyUpdate(node, tl, tr);

	if (tree[node]+v < L || tr < 1){
        return -1;
	}
	if (tl == tr){
        return tl;
	}
	int mid = (tl+tr)/2;
	int left = query(node*2, tl, mid, v);
	if (left != -1) return left;
	return query(node*2+1, mid+1, tr, v+tree[node*2]);
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N, M, l, r, m;
    cin >> N >> M >> L;
    for(int i = 1; i<=N; i++)
        A[i] = 1;
    build(1, 1, N);
    for(int i = 0; i<M; i++){
        cin >> l >> r;
        update(1, 1, N, l, r);
        int res = query(1, 1, N, 0);
        if (res == -1) cout << "AC?\n";
        else cout << query(1, 1, N, 0) << "\n";
    }
}