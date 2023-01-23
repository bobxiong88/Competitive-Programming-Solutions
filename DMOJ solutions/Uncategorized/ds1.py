import sys
input = sys.stdin.readline
def update(index, value, tree, array):
    while index < len(array):
        tree[index] += value
        index += index & -index
def get_sum(index, tree):
    ans = 0
    while index > 0:
        ans += tree[index]
        index -= index& -index
    return ans
def range_sum(left, right, tree):
    return get_sum(right, tree) - get_sum(left-1, tree)
N, M = map(int,input().split())
array = list(map(int,input().split()))
array.insert(0,0)
frequency = [0 for i in range(100001)]
sumTree = [0 for i in range(N+1)]
countTree = [0 for i in range(100001)]
for i in range(1, N+1):
    update(i, array[i], sumTree, array)
    frequency[array[i]] += 1
for i in range(1, 100001):
    update(i, frequency[i], countTree, frequency)
for i in range(M):
    query = input()
    if query[0] == "C":
        _, x, v = query.split()
        x, v = map(int,[x,v])
        update(array[x], -1, countTree, frequency)
        update(v, 1, countTree, frequency)
        update(x, v-array[x], sumTree, array)
        array[x] = v
    elif query[0] == "S":
        _, l, r = query.split()
        l,r = map(int,[l,r])
        print(range_sum(l, r, sumTree))
    else:
        _, v = query.split()
        v = int(v)
        print(get_sum(v,countTree))