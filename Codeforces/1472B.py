import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    x = a.count(1)
    y = a.count(2)
    ans = 'YES'
    s = sum(a)
    if s%2:
        ans = 'NO'
    c = 0
    while c < s//2:
        d = s//2 -c
        if d == 1 and not x:
            ans = 'NO'
            break
        else:
            c+=2
            if y:
                y-=1
            else:
                x-=2
    print(ans)
