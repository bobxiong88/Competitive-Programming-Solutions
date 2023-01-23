import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    freq = [0]*26
    for i in s:
        freq[ord(i)-ord('a')] += 1
    ans = 0
    sin = 0
    for i in freq:
        if i == 1:
            sin += 1
        if i >= 2:
            ans += 1
    ans += sin//2
    print(ans)
