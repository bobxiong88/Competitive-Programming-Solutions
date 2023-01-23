import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = 3
    ans = 0
    while (a**2+1)//2 <= n:
        if (a**2+1)/2 == (a**2+1)//2:
            ans += 1
        a += 1
    print(ans)
