import sys
input = sys.stdin.readline
n = int(input())
s = input().strip('\n')
name = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
for x in name:
    if len(x) == n:
        f = True
        for i in range(n):
            if s[i]!='.' and s[i]!=x[i]:
                f = False
                break
        if f:
            print(x)
            break
