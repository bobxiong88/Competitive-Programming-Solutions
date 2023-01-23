import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    s = list(s)
    s = [int(i) for i in s]
    s.append(0)
    i = 0
    ans = 0
    start = -1
    while any(s):
        i+=1
        con = []
        for x in range(len(s)):
            if s[x] == 1 and start == -1:
                start = x
            if s[x] == 0 and start != -1:
                con.append((start, x-1, x-start))
                start = -1
        con.sort(key = lambda x: x[2])
        a,b,c = con[-1]
        s = s[:a]+s[b+1:]
        if i%2: ans += c
    print(ans)
