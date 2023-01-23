import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    found = [False for i in range(n+1)]
    for i in range(n-1):
        s = a[i]
        for j in range(i+1,n):
            s+=a[j]
            if s>n: break
            found[s] = True
    c = 0
    for i in a:
        if found[i]: c+=1
    print(c)
