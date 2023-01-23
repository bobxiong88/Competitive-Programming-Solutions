import sys
input = sys.stdin.readline
def dfs(p,arr, d):
    if not arr:
        return
    m = max(arr)
    x = arr.index(m)
    a = arr[:x]
    b = arr[x+1:]
    #print(a, b)
    #print(p, arr, d)
    ans[p+x] = d
    dfs(p, a, d+1)
    dfs(p+x+1, b, d+1)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*n
    dfs(0 ,a, 0)
    print(*ans)
