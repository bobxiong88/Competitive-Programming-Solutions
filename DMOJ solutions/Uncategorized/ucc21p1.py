import sys
input = sys.stdin.readline
s = input().strip('\n')
cnt=0
N = len(s)
for i in range(N):
    if s[i] == '2':
        if i == N-1:
            cnt += 1
        elif s[i+1]!='5':
            cnt += 1
print(cnt)