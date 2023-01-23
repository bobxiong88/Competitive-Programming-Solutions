import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, a, b = map(int,input().split())
    s = input().strip('\n')
    ans = a*len(s)
    if b >= 0:
        print(ans+b*len(s))
    else:
        curr = s[0]
        nw = []
        for i in range(n):
            if s[i] == curr:
                pass
            else:
                nw.append(curr)
            curr = s[i]
        if (not nw) or nw[-1]!=curr:
            nw.append(curr)
        print(ans+b*(len(nw)//2+1))
