import sys
input = sys.stdin.readline
for _ in range(int(input())):
    def opp(c):
        if c == 'R': return 'B'
        return 'R'
    n = int(input())
    a = list(input().strip('\n'))
    i = 0
    while i< n and a[i] == '?':
        i+=1
    if i == n:
        res = ''
        for i in range(n):
            if i%2 == 0: res += 'B'
            else: res += 'R'
        print(res)
    else:
        if i > 0:
            for j in range(i-1, -1, -1):
                if (i-j)%2 == 0:
                    a[j] = a[i]
                else:
                    a[j] = opp(a[i])
        last = a[i]
        for j in range(i+1, n):
            if a[j] == '?':
                if (i-j)%2 == 0:
                    a[j] = a[i]
                else:
                    a[j] = opp(a[i])
            else:
                last = a[j]
                i = j
        print(''.join(a))
