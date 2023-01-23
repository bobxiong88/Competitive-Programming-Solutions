import sys
input = sys.stdin.readline
ans = [0]*5005
for i in range(1,5005):
    if int((i-1)**0.5) == (i-1)**0.5:
        ans[i] = ans[i-1]+1
    else:
        ans[i] = ans[i-1]
for _ in range(int(input())):
    print(ans[int(input())])
