import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    word = []
    for i in range(n):
        s = input().strip('\n')
        freq = [0]*5
        for x in s: freq[ord(x)-ord('a')] += 1
        word.append(freq)
    ans = 0
    for x in range(5):
        baka = []
        res = 0
        coc = 0
        for f in word:
            t = sum(f)
            t -= f[x]
            if f[x] > t:
                coc += f[x]-t
                res += 1
            else:
                baka.append(t-f[x])
        baka.sort()
        for i in range(len(baka)):
            if coc-baka[i] <= 0:
                break
            else:
                coc -= baka[i]
                res += 1
        #print(res, x, baka)
        ans = max(res, ans)
    print(ans)
