import sys
input = sys.stdin.readline
letters = 'abcdefghijklmnopqrstuvwxyz'
N = int(input())
L = int(input())%26
S = input()[:N]
ans = ""
for i in S:
    if i==" ":
        ans = ans + i
        continue
    ans = ans + letters[(letters.index(i)+L)%26]
print(ans)