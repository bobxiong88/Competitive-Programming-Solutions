import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    pos = [[0,0] for i in range(n)]
    pos[0] = [h[0],h[0]]
    ans = 'YES'
    for i in range(1,n):
        pos[i][0] = max(h[i],pos[i-1][0]-k+1)
        pos[i][1] = min(h[i]+k-1,pos[i-1][1]+k-1)
        if pos[i][0]-h[i] >= k:
            ans = 'NO'
        if h[i] >= (pos[i-1][1]+k):
            ans = 'NO'
        if pos[i][0] > pos[i][1]:
            ans = 'NO'
    if not(pos[-1][0]<=h[-1]<=pos[-1][1]):
        ans = 'NO'
    print(ans)
            
    #print(pos)
