import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().strip('\n')
    ans = []
    for i in range(len(s)):
        if i%2==0:
            ans.append(s[i])
    ans.append(s[-1])
    print("".join(ans))
