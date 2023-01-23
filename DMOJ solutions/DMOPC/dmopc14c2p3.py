import sys
input = sys.stdin.readline
N = int(input())
saw = list(map(int,input().split()))
log = list(map(int,input().split()))
saw.sort()
log.sort(reverse = True)
ans = 0
for i in range(N): ans += saw[i]*log[i]
print(ans)