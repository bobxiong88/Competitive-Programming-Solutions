import sys
input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    cnt = [[] for i in range(26)]
    for i in range(n):
        cnt[ord(s[i])-ord('a')].append(i)
    a = ord(s[0])-ord('a')
    b = ord(s[-1])-ord('a')
    res = []
    le = 0
    if a <= b:
        for i in range(a, b+1):
            if cnt[i]:
                res.append(' '.join([str(j+1) for j in cnt[i]]))
                le += len(cnt[i])
    else:
        for i in range(a, b-1, -1):
            if cnt[i]:
                res.append(' '.join([str(j+1) for j in cnt[i]]))
                le += len(cnt[i])
    print(abs(b-a), le)
    print(' '.join(res))
    
