# monotonic queue madness
import sys
input = sys.stdin.readline
N = int(input())
a = tuple(int(input()) for i in range(N))
stack, ans = [], 0
for i in range(N):
    n, c = 1, 1
    remove = False
    while stack:
        if stack[-1][0]<=a[i]:
            poo = stack.pop()
            if poo[0]==a[i]: c+=poo[1]
            n+=poo[1]
            remove = True
        else: remove = False; break
    if remove: n-=1
    stack.append((a[i], c))
    if i: ans+=n
print(ans)