import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    cnt = 0

    change = [False]*n

    ans = 0

    for i in range(1,n-1):
        p = 0
        if a[i-1]>a[i]<a[i+1]:
            cnt += 1
            change[i] = True
        if a[i-1]<a[i]>a[i+1]:
            cnt += 1
            change[i] = True
        k = 0
        m = 0
        # change to right
        if i+2 < n:
            if (a[i] < a[i+1] > a[i+2]) or (a[i] > a[i+1] < a[i+2]):
                k += 1
        if i-2 >= 0:
            if change[i-1]:
                if not ((a[i-2] < a[i-1] > a[i+1]) or (a[i-2] > a[i-1] < a[i+1])):
                    k+=1
            else:
                if (a[i-2] < a[i-1] > a[i+1]) or (a[i-2] > a[i-1] < a[i+1]):
                    k-=1

        #change to left
        if i-2 >= 0:
            if change[i-1]:
                m += 1
        if i+2 < n:
            if (a[i] < a[i+1] > a[i+2]) or (a[i] > a[i+1] < a[i+2]):
                if not ((a[i-1] < a[i+1] > a[i+2]) or (a[i-1] > a[i+1] < a[i+2])):
                    m+=1
            else:
                if (a[i-1] < a[i+1] > a[i+2]) or (a[i-1] > a[i+1] < a[i+2]):
                    m-=1
        if change[i]:
            p += 1
        p += max(m,k)
        ans = max(ans, p)
        #print(p, cnt)
    print(cnt-ans)
