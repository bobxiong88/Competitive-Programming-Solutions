import sys
input = sys.stdin.readline
from math import log
from math import ceil
from collections import deque
def check(n, k):
    n >>= k
    return n&1
def cv(n, K):
    return ['0']*(K-len(list(bin(n)[2:])))+list(bin(n)[2:])
K = int(input())
piss = K
a = [input().strip('\n') for i in range(K)]
vis = set()
n = int(''.join(a), 2)
vis.add(n)
queue = deque([(n,0)])
ans = float('inf')
while queue:
    n,cnt = queue.popleft()
    if n == 0:
        ans = min(cnt, ans)
        break
    K = max(4,ceil(log(n, 2)))
    b = cv(n, K)
    p = 0
    while b[-1] == '0' and len(b) > 4:
        b.pop()
        n >>= 1
        K-=1
    if len(b) == 4:
        ans = min(ans, cnt + b.count('0'))
        if piss > 20: break
        continue
    #print(cv(n, K), n, cnt)
    for i in range(K):
        if not check(n, i):
            new = n|(2**i)
            if new not in vis:
                vis.add(new)
                b = cv(new, K)
                c = 0
                for j in range(K):
                    if b[j] == '1':
                        c += 1
                    else:
                        if c >= 4:
                            for z in range(j-c,j): b[z] = '0'
                            c = 0
                            break
                        c = 0
                if c >= 4:
                    for z in range(K-c,K):
                        b[z] = '0'
                new = int(''.join(b), 2)
                queue.append((new, cnt+1))
print(ans)