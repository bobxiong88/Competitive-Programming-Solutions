# i < j, a_i < a_j, no connections
# i < j, a_i >= a_j, connection possible
# number of inversions, except including the ones that are equal?

import sys
input = sys.stdin.readline
def LSB(x):
    return x & (-x)
def get_sum(x):
    res = 0
    while x > 0:
        res += bit[x]
        x -= LSB(x)
    return res
def add(x):
    while x < len(bit):
        bit[x] += 1
        x += LSB(x)
for _ in range(int(input())):
    n = int(input())
    a = [0]+list(map(int,input().split()))
    bit = [0]*(n+1)
    ans = 0
    for i in range(1,n+1):
        #print(i, a[i], get_sum(a[i]-1))
        ans += i-get_sum(a[i]-1)-1
        add(a[i])
    print(ans)
