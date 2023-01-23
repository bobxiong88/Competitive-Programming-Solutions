import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, c = map(int,input().split())
    a = list(map(int,input().split()))
    freq = [0]*101
    for i in a:
        freq[i] += 1
    ans = 0
    for i in range(101):
        ans += min(freq[i],c)
    print(ans)
