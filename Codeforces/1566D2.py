import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    freq = dict()
    lol = []
    for i in range(n*m):
        if a[i] in freq:
            freq[a[i]].append(i)
        else:
            freq[a[i]] = [i]
            lol.append(a[i])
    lol.sort()
    dab = []
    has = [[0]*m for i in range(n)]
    prev = 0
    i = 0
    j = 0
    for x in lol:
        freq[x].sort(reverse = True)
        curr = []
        while freq[x]:
            curr.append(freq[x].pop())
            if j == m-1:
                curr = curr[::-1]
                while curr:
                    has[i][j] = curr.pop()
                    j -= 1
                j = -1
                i += 1
                curr = []
            j += 1
        if curr:
            curr = curr[::-1]
            for y in range(j-1,-1,-1):
                if not curr: break
                has[i][y] = curr.pop()
    ans = 0
    for x in range(n):
        for i in range(m):
            for j in range(i):
                if has[x][i] > has[x][j]:
                    ans += 1
    print(ans)
