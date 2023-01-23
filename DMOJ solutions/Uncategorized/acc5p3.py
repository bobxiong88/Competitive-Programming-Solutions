N, K = map(int,raw_input().split())
a = []
ans = 0
for i in range(N):
    p, d = map(int,raw_input().split())
    a.append(p-d)
    ans += p
a.sort(reverse = True)
ans -= sum(a[:K])
print(ans)