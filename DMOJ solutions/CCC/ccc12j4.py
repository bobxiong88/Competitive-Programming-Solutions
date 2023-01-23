import sys
input = sys.stdin.readline
K = int(input())
s = input().strip('\n')
for i in range(len(s)):
    x = 3*(i+1)+K
    pos = ord(s[i])-65
    pos -= x
    pos %= 26
    pos += 65
    print(chr(pos),end = '')