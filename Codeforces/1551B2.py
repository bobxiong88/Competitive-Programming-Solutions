import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    freq = [[] for i in range(n+1)]
    for i in range(n):
        freq[a[i]].append(i)
    sus = []
    ans = [0]*n
    for x in range(1,n+1):
        if len(freq[x]) < k:
            for i in freq[x]: sus.append(i)
        else:
            if k > 1:
                for i in range(k):
                    ans[freq[x][i]] = i%k+1
            else:
                ans[freq[x][0]] = 1
    for i in range(len(sus)-len(sus)%k):
        ans[sus[i]] = i%k+1
    print(*ans)
