import sys
input = sys.stdin.readline
a = input().strip('\n')
b = input().strip('\n')
n = len(b)
ans = set()
for i in range(n+1):
    for j in a:
        ans.add(b[:i]+j+b[i:])
for i in range(n):
    for j in a:
        ans.add(b[:i]+j+b[i+1:])
for i in range(n):
    ans.add(b[:i]+b[i+1:])
ans = list(ans)
for i in sorted(ans):
    if i == b: continue
    print(i)