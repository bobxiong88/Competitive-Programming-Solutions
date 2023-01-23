import sys
input = sys.stdin.readline
n = input().strip('\n')
while n != '99999':
    a = sum(list(map(int,n[:2])))
    b = int(n[2:])
    if a == 0:
        print("{} {}".format(pre, b))
    else:
        print("{} {}".format('left' if a%2 else 'right', b))
    pre = 'left' if a%2 else 'right'
    n = input().strip('\n')