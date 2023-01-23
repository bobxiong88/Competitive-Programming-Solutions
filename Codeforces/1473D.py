import sys
input = sys.stdin.readline
for _ in range(int(input())):
    psa = [0]

    n,m = map(int,input().split())
    mx = [0]*(n+1)
    mn = [0]*(n+1)
    mx2 = [0]
    mn2 = [0]
    s = input().strip('\n')
    for i in range(n):
        if s[i] == '+': k = 1
        else: k = -1
        psa.append(psa[-1]+k)
        mx2.append(max(mx2[-1],psa[-1]))
        mn2.append(min(mn2[-1],psa[-1]))
    for i in range(n,-1,-1):
        if i == n:
            mx[i] = psa[i]
            mn[i] = psa[i]
        else:
            mx[i] = max(mx[i+1],psa[i])
            mn[i] = min(mn[i+1],psa[i])
    mx.append(mx[-1])
    mn.append(mn[-1])
    for i in range(m):
        l,r = map(int,input().split())
        v = psa[l-1]
        x = mx[r+1]-psa[r]
        y = mn[r+1]-psa[r]
        #print(v,x,y)
        print(max(v+x, mx2[l-1])-min(v+y,mn2[l-1])+1)
