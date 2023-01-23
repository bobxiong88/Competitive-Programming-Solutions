import sys
input = sys.stdin.readline
for _ in range(int(input())):
    line = input().strip('\n')
    c = line[0]
    cnt = 1
    ans = []
    for x in line[1:]:
        if x != c:
            ans.append(str(cnt))
            ans.append(c)
            cnt = 0
        cnt += 1
        c = x
    ans.append(str(cnt))
    ans.append(c)
    print(' '.join(ans))