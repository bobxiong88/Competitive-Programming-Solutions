import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = list(set(a))
    if len(a)>k:
        print(-1)
        continue
    b = []
    for i in range(n):
        b = b+a+(k-len(a))*[1]
    print(len(b))
    print(*b)
