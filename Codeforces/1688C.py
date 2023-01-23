import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    t = [input().strip() for i in range(n*2)]
    s = input().strip()
    t.append(s)
    freq = [0]*26
    for s in t:
        for i in s:
            freq[ord(i)-ord('a')]+=1
    for i in range(26):
        if freq[i]%2:
            print(chr(i+ord('a')))
            break
