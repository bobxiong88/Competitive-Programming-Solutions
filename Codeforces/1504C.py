import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip('\n')
    if not (s[0] == s[-1] == '1'):
        print('NO')
        continue
    same = []
    diff = []
    for i in range(n):
        if s[i] == '1':
            same.append(i)
        else:
            diff.append(i)
    if len(same)%2:
        print('NO')
        continue
    a = ['0']*n
    b = ['0']*n
    k = len(same)
    for i in range(k//2):
        a[same[i]] = '('
        b[same[i]] = '('
    for i in range(k//2,k):
        a[same[i]] = ')'
        b[same[i]] = ')'
    k = len(diff)
    for i in range(k):
        if i%2:
            a[diff[i]] = '('
            b[diff[i]] = ')'
        else:
            a[diff[i]] = ')'
            b[diff[i]] = '('
    print('YES')
    print(''.join(a))
    print(''.join(b))
