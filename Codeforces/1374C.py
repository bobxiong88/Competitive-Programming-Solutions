import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    op = 0
    cl = 0
    ans = 0
    for i in range(n):
        if s[i] == "(":
            op+=1
        else:
            cl+=1
            if cl>op:
                ans = max(ans, cl-op)
    print(ans)
