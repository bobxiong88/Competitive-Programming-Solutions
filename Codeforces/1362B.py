import sys
input = sys.stdin.readline
mx = 10
def b(n):
    return '0'*(mx-len(bin(n)[2:]))+bin(n)[2:]
for _ in range(int(input())):
    n = int(input())
    s = set(map(int,input().split()))
    ans = -1
    for i in range(1, 1024):
        a = [j^i for j in s]
        if set(a) == s:
            ans = i
            break
    print(ans)
