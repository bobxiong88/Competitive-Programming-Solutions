import sys
input = sys.stdin.readline
def check(t):
    a = 0
    b = 0
    for i in range(10):
        if (i+1)%2:
            a += int(t[i])
        else:
            b += int(t[i])
        pa = (10-i-1)//2
        pb = (10-i)//2
        #print(i, pa,pb, a, b)
        if a+pa < b or b+pb < a:
            return i+1
    return 10
for _ in range(int(input())):
    s = list(input().strip('\n'))
    a = []
    for i in range(10):
        if s[i] == '?':
            a.append(i)
    tot = []
    ans = 10
    for i in range(2**len(a)):
        curr = s[:]
        for j in range(len(a)):
            curr[a[j]] = i&1
            i >>= 1
        ans = min(ans, check(curr))
    print(ans)
    
