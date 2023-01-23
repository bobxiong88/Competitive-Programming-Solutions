import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if n%2:
        print("NO")
    else:
        b = []
        for i in range(n//2):
            b.append(a[i])
            b.append(a[i+n//2])
        b = b+b
        ans = "YES"
        for i in range(n):
            if not(b[i-1] < b[i] > b[i+1] or b[i-1] > b[i] < b[i+1]):
                ans = "NO"
        print(ans)
        if ans == "YES":
            print(*b[:n])
