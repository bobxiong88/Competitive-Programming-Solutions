import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    freq = [[] for i in range(n+1)]
    for i in range(n):
        freq[a[i]].append(i+1)
    ans = -1
    for i in range(1,n+1):
        if len(freq[i])==1:
            ans = freq[i][0]
            break
    print(ans)
