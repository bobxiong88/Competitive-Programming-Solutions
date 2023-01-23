import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    diff = []
    for i in range(n-1):
        diff.append(a[i+1]-a[i])
    curr = False
    if diff[0]>0:
        curr = True
    b = [a[0]]
    for i in range(1,n-1):
        if diff[i]>0 and not curr:
            b.append(a[i])
            curr = True
        if diff[i]<0 and curr:
            b.append(a[i])
            curr = False
    if a[-1] not in b:
        b.append(a[-1])
    print(len(b))
    print(" ".join([str(i) for i in b]))
