import sys
input = sys.stdin.readline
s = input().strip('\n')
for i in range(len(s)-3):
    if s[i:i+4]=='java':
        print(i)
        sys.exit(0)
print(len(s))