# dcordb's solution idea
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx = max(a)
    ans = ['a'*(mx+1) for i in range(n+1)]
    for i in range(n):
        s = 'a' if ans[i][a[i]] == 'b' else 'b'
        ans[i+1] = ans[i][:a[i]] + s + ans[i][a[i]+1:]
    for i in ans: print(i)
    
