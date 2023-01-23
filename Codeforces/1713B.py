import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    real = [a[0]]
    for i in a:
        if i != real[-1]:
            real.append(i)
    a = real[:]
    n = len(a)
    ans = "YES"
    for i in range(1,n-1):
        if a[i-1] > a[i] < a[i+1]:
            ans= "NO"
    print(ans)
