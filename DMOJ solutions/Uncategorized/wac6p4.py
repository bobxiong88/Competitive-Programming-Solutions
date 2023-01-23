import sys
input = sys.stdin.readline
m = 998244353
N, K = map(int,input().split())
s = input().strip('\n')
W = s.count('W')
C = s.count('C')
w = [0]*(N+1)
c = [0]*(N+1)
one = [0]*(K+1)
for i in range(K+1):
    if not i: continue
    one[i] = one[i-1]+i
    one[i] %= m
val = [0]*(K+1)
for i in range(K+1):
    val[i] = i*(K-1-i)+val[i-1]
for i in range(N):
    w[i] = w[i-1]+int(s[i] == 'W')
for i in range(N-1, -1, -1):
    c[i] = c[(i+1)%N] + int(s[i] == 'C')

ans = 0
for i in range(N):
    if s[i] == 'A':
        ans += w[i]*c[i]*K
        ans += c[i]*one[K-1]*W
        ans += one[K-1]*C*w[i]
        ans += val[K-1]*W*C
        ans %= m
print(ans)