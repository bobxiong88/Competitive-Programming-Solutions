import sys
input = sys.stdin.readline
def get(x):
    return chr(ord('a')+x)
for _ in range(int(input())):
    s = list(input().strip('\n'))
    n = len(s)
    if 'a' in s:
        l = s.index('a')
        r = l
    else:
        print("NO")
        continue
    if len(set(s)) < n:
        print("NO")
        continue
    pos = True
    for i in range(n-1):
        if l-1 >= 0 and s[l-1] == get(i+1):
            l = l-1
        elif r+1 < n and s[r+1] == get(i+1):
            r = r+1
        else:
            pos = False
            break
    if not pos:
        print("NO")
    else:
        print("YES")
