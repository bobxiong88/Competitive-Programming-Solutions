import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    a = s.index('(')
    b = s.index(')')
    ans = 'YES'
    if a == len(s)-1 or b == 0:
        ans = 'NO'
    else:
        if (len(s)-2)%2:
            ans = 'NO'
    print(ans)
