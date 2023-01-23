import sys
input = sys.stdin.readline
for _ in range(int(input())):
    def check(k):
        if k+1 > n:
            ans = 0
            tot = sum(a)
            ans = tot*(d//(k+1))+sum(a[:min(n, d%(k+1))])
            #print(ans)
            return ans >= c
        else:
            ans = 0
            tot = sum(a[:k+1])
            ans = tot*(d//(k+1))+sum(a[:d%(k+1)])
            #print(ans)
            return ans >= c
    n,c,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    if sum(a[:min(n,d)]) >= c:
        print("Infinity")
        continue
    if check(0) == False:
        print("Impossible")
        continue
    l = 0
    r = d
    ans = 0
    while l <= r:
        k = (l+r)//2
        if check(k):
            ans = max(ans,k)
            l = k+1
        else:
            r = k-1
    print(ans)
    
