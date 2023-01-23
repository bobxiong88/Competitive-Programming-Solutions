import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = []
    if n == 1:
        print(9)
    elif n == 2:
        print(98)
    elif n==3:
        print(989)
    else:
        ans = ['989']
        n -= 3
        for i in range(n):
            ans.append(str(i%10))
        print(''.join(ans))
