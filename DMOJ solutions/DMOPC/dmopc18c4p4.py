import sys
input = sys.stdin.readline
def update(index, value):
    while index < len(array):
        tree[index] += value
        index += index & -index
def get_sum(index, tree):
    ans = 0
    while index > 0:
        ans += tree[index]
        index -= index& -index
    return ans
def range_sum(left, right):
    return get_sum(right, tree) - get_sum(left-1, tree)
N, Q = map(int,input().split())
array = [int(i) for i in input().split()]
array.insert(0,0)
order = [(array[i], i) for i in range(N+1)]
order.sort(key = lambda x: x[0])
prefix = [0]*(N+1)
for i in range(1,N+1): prefix[i] = prefix[i-1]+array[i]
tree = [0 for i in range(N+1)]
q, ans = [], [0 for i in range(Q)]
for x in range(Q):
    l,r,k = map(int,input().split())
    q.append((l,r,k,x))
q.sort(key = lambda x: x[2], reverse = True)
for l, r, k, x in q:
    while order and order[-1][0]>=k:
        v, i = order.pop()
        update(i, v)
    ans[x] = str(2*range_sum(l,r)-(prefix[r]-prefix[l-1]))
print("\n".join(ans))