import sys
input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if N%2:
        print(*a)
    else:
        ans = [0]*N
        a1 = []
        a2 = []
        for i in range(N):
            if i<int(N/2):
                a1.append(a[i])
            else:
                a2.append(a[i])
        for i in range(int(N/2)):
            ans[i*2] = a1[i]
            ans[i*2+1] = a2[i]
        if len(set(ans)) == 1:
            print(-1)
        else:
            print(*ans)