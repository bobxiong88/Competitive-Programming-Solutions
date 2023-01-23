import sys
input = sys.stdin.readline
w = int(input())
ans = "NO"
for i in range(2,w):
    if i%2==0 and (w-i)%2==0:
        ans = "YES"
print(ans)