import sys
input = sys.stdin.readline
s = input().strip('\n')
n = len(s)
kevin = []
last = s[0]
cnt = 0
for i in range(n):
    if s[i] == last:
        cnt += 1
    else:
        kevin.append((last, cnt))
        cnt = 1
    last = s[i]
if cnt:
    kevin.append((last, cnt))
if len(kevin)%2==0:
    print(0)
    sys.exit(0)
k = len(kevin)//2
if kevin[k][1] < 2:
    print(0)
    sys.exit(0)

pos = True
for i in range(k):
    if not(kevin[i][0] == kevin[~i][0] and kevin[i][1]+kevin[~i][1] >= 3):
        pos = False
        break
if pos:
    print(kevin[k][1]+1)
else:
    print(0)
