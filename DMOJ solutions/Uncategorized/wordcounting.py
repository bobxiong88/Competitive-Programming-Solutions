import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
p = list(map(int,input().split()))
w = list(map(int,input().split()))
monkey = [(w[i], i) for i in range(Q)]
monkey.sort(reverse = True)
ans = [0]*Q
racism = sorted([(p[i], i+1) for i in range(N)])
racism.append((100000000000, 100000000000))
s = []
for i in range(len(racism)):
    if i == 0 or racism[i][0] != racism[i-1][0]:
        s.append(racism[i])
for i in range(len(s)-1):
    x = s[i][0]*s[i+1][0]
    if not monkey: break
    while monkey and monkey[-1][0] <= x:
        a, b = monkey.pop()
        ans[b] = s[i][1]
        if a == x: ans[b] = min(ans[b], s[i+1][1])
print(' '.join([str(i) for i in ans]))