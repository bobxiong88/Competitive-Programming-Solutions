import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = input().strip('\n')
    b = input().strip('\n')
    ans = len(a)+len(b)
    p = 37
    m = 2828285675343
    pp = [1]*30
    for i in range(1,30):
        pp[i] = pp[i-1]*p
        pp[i] %= m
    for i in range(len(a)):
        s = ''
        hs1 = 0
        for j in range(i, len(a)):
            s += a[j]
            hs1 += ord(a[j])*pp[j-i]
            hs1 %= m
            for k in range(len(b)):
                t = ''
                hs2 = 0
                for l in range(k, len(b)):
                    t += b[l]
                    hs2 += ord(b[l])*pp[l-k]
                    hs2 %= m
                    if hs1 == hs2:
                        ans = min(ans, len(a)-len(s)+len(b)-len(t))
    print(ans)
