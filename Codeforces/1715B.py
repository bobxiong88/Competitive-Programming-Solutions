import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k, b, s = map(int,input().split())
    big = s-(n-1)*(k-1)
    minb = big//k
    maxb = s//k
    #print(minb,maxb)
    if not minb <= b <= maxb:
        print(-1)
        continue
    ans = []
    for i in range(n):
        res = s-i*(k-1)
        if res//k==b:
            ans = [res]+i*[k-1]+(n-1-i)*[0]
            break
    print(*ans)
