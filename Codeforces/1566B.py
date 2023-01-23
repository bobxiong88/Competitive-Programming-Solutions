import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    n = len(s)
    if '1' not in s:
        print(1)
    elif '0' not in s:
        print(0)
    else:
        meme = []
        last = s[0]
        for i in range(n):
            if s[i] != last:
                meme.append(last)
            last = s[i]
        if meme and meme[-1] != last:
            meme.append(last)
        print(min(meme.count('0'),2))
