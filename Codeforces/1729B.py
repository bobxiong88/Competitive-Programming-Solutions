import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = []
    for i in range(n):
        if s[i] == '0' and not (i < n-1 and s[i+1]=='0'):
            a = ans.pop(-1)
            b = ans.pop(-1)
            ans.append(b+a)
        else:
            ans.append(s[i])
    print(''.join([chr(96+int(i)) for i in ans]))
    
