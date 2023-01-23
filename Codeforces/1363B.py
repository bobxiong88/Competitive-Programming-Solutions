import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    s1 = '010'
    s2 = '101'
    n = len(s)
    ans = float('inf')
    cz = []
    co = [0]*(n+1)
    c = 0
    for i in range(n):
        if s[i]!='0':
            c+=1
        cz.append(c)
    c = 0
    for i in range(n-1,-1,-1):
        if s[i]!='1':
            c+=1
        co[i] = c
    for i in range(n):
        ans = min(ans, cz[i]+co[i+1])
        
    cz = []
    co = [0]*(n+1)
    c = 0
    for i in range(n):
        if s[i]!='1':
            c+=1
        cz.append(c)
    c = 0
    for i in range(n-1,-1,-1):
        if s[i]!='0':
            c+=1
        co[i] = c
    for i in range(n):
        ans = min(ans, cz[i]+co[i+1])
    

    print(ans)
