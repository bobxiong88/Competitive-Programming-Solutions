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
N = int(input())
array = [0]+[int(i) for i in input().split()]
order = [(array[i], i) for i in range(N+1)]
order.sort(key = lambda x: x[0])
tree = [0 for i in range(N+1)]
Q = int(input())
q, ans = [], [0 for i in range(Q)]
for x in range(Q):
    l,r,k = map(int,input().split())
    q.append((l+1,r+1,k,x))
q.sort(key = lambda x: x[2], reverse = True)
for l, r, k, x in q:
    while order and order[-1][0]>=k:
        v, i = order.pop()
        update(i, v)
    ans[x] = str(range_sum(l,r))
print("\n".join(ans))