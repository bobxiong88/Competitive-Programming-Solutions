import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = []
    t = n-k
    p = [i for i in range(1,k+1)]
    g = p[k-t-1:]
    p = p[:k-t-1]+g[::-1]
    print(*p)
    '''
    x = 1
    for i in range(1,n+1):
        if k <i:
            a.append(k-x)
        else:
            a.append(i)
    '''
    #print(*a)
