import sys
input = sys.stdin.readline
while True:
    r = int(input())
    ans = 0
    if not r: break
    for y in range(r-1, 0, -1):
        res = int((r**2-y**2)**0.5)
        ans += res*4
    ans += r*4+1
    print(ans)