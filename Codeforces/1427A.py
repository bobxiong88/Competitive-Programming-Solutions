import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if sum(a) == 0:
        print("NO")
        continue
    print("YES")
    one = []
    two = []
    zero = []
    for i in a:
        if i>0: one.append(i)
        elif i<0: two.append(i)
        else: zero.append(i)
    if sum(one)>abs(sum(two)): one = one+two
    else: one = two + one
    one = one + zero
    print(*one)
