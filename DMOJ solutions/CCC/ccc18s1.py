N = int(input())
a = [int(input()) for i in range(N)]
a.sort()
ans = float('inf')
for i in range(1,N-1):
    ans = min(ans, (a[i]-a[i-1]+a[i+1]-a[i])/2)
print(ans)