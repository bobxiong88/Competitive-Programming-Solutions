import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    even = []
    odd = []
    for i in range(n):
        if a[i]%2:
            odd.append(a[i])
        else:
            even.append(a[i])
    even.sort()
    odd.sort()
    s = [0,0]
    i = 0
    while even or odd:
        t = i%2
        if even and (not odd or even[-1] > odd[-1]):
            if t == 0:
                s[t] += even.pop()
            else:
                even.pop()
        else:
            if t == 1:
                s[t] += odd.pop()
            else:
                odd.pop()
        i+=1
    if s[0] == s[1]:
        print('Tie')
    elif s[0] > s[1]:
        print('Alice')
    else:
        print('Bob')
