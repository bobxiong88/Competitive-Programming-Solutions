import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
sub = []
for i in range(10):
    for j in range(10):
        sub.append((i,j))
for _ in range(t):
    s = list(input())
    s = [int(s[i]) for i in range(len(s)-1)]
    ans = float('inf')
    if len(s)<=2:
        print(0); continue
    for a,b in sub:
        new = []
        for i in s:
            if i==a or i==b: new.append(i)
        n = len(new)
        c = len(s)-n
        new = deque(new)
        d = (a,b)
        nn = []
        while new:
            curr = new.popleft()
            if nn:
                if nn[-1]!=curr:
                    nn.append(curr)
            else:
                nn.append(curr)
        c+=n-len(nn)
        if len(nn)%2:
            c+=1
        ans = min(ans, c)
    for i in range(10):
        ans = min(ans, len(s)-s.count(i))
    print(ans)
