import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    s = []
    if b==0:
        if a:
            s = [0]*(a+1)
        else:
            s = [1]*(c+1)
    else:
        for i in range(b+1):
            if i%2:
                s.append(0)
            else:
                s.append(1)
        s = [1]*(c)+s
        for i, x in enumerate(s):
            if not x:
                break
        s = s[:i]+[0]*a+s[i:]
    print("".join([str(i) for i in s]))
        
