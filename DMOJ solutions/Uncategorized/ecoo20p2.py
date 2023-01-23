import sys
input = sys.stdin.readline
for _ in range(int(input())):
    ans = 0
    N = int(input())
    d = {}
    for x in range(N):
        M = int(input())
        for i in range(M):
            S, P, Q = input().split()
            P, Q = int(P), int(Q)
            if S in d: d[S].append((P, Q))
            else: d.update({S:[(P, Q)]})
    K = int(input())
    for i in range(K):
        S, D = input().split()
        D = int(D)
        d[S].sort(key = lambda x: x[0])
        for P, Q in d[S]:
            if D >= Q:
                ans += P*Q
                D -= Q
            else:
                ans += P*D
                break
    print(ans)