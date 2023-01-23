import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = tuple(map(int,input().split()))
    found = False
    for i in range(1,n-1):
        if a[i-1]<a[i]>a[i+1]:
            found = True
            break
    if not found:
        print("NO")
        continue
    print("YES")
    print(i-1+1,i+1,i+1+1)
