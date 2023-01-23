import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    t = input().strip('\n')
    a = len(s)
    b = len(t)
    ans = 0
    for i in range(1,b+1):
        if t*(a*i//b) == s*i:
            ans = s*i
            break
    if not ans: ans = -1
    print(ans)
            
