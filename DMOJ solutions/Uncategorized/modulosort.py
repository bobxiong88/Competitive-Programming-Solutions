import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
a = list(map(int,input().split()))
mod = dict()
for i in range(N):
    if a[i]%K in mod:
        mod[a[i]%K].append(a[i])
    else:
        mod[a[i]%K] = [a[i]]
for i in sorted(mod.keys()):
    print(*sorted(mod[i]), end = ' ')