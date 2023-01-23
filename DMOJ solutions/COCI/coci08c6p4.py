import sys
from math import ceil
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
mod = [[],[],[]]
for x in a: mod[x%3].append(x)
if len(mod[0]) > ceil(n/2):
    print("impossible")
    sys.exit(0)
ans = []
while mod[0]:
    ans.append(mod[0].pop())
    if mod[1]: ans.append(mod[1].pop())
    elif mod[2]: ans.append(mod[2].pop())
if not ans:
    if mod[1] and mod[2]: print("impossible")
    else: print(*a)
    sys.exit(0)
if ans[-1]%3 == 0: pass
elif ans[-1]%3 == 1: ans = mod[2]+ans+mod[1]
else: ans = mod[1]+ans+mod[2]
print(*ans)