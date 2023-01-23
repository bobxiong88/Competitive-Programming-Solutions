# monotonic queue madness
import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
stack, ans = [], ['0']*N
for i in range(N):
    while stack and stack[-1][0]<=a[i]:
        stack.pop()
    ans[i] = str(i-stack[-1][1]) if stack else str(i)
    stack.append((a[i], i))
print(" ".join(ans))