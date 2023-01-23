import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    s = [list(input().strip('\n')) for i in range(n)]
    ans = s[0][:]
    for x in range(m):
        curr = str(ans[x])
        for i in range(97, 123):
            ans[x] = chr(i)
            found = True
            for j in range(n):
                c = 0
                for y in range(m):
                    if ans[y]!=s[j][y]:
                        c+=1
                if c>1: found = False
                #print(''.join(ans), ''.join(s[j]), c)
            if found:
                print(''.join(ans))
                break
        if found: break
        ans[x] = curr
    if not found: print(-1)
