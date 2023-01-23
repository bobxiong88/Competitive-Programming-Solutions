import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip('\n')
    ans = 'NO'
    if s[:4] == '2020':
        ans = 'YES'
    if s[:1] == '2':
        if s[-3:] == '020':
            ans = 'YES'
    if s[:2] == '20':
        if s[-2:] == '20':
            ans = 'YES'
    if s[:3] == '202':
        if s[-1:] == '0':
            ans = 'YES'
    if s[-4:] == '2020':
        ans = 'YES'
    print(ans)
        
