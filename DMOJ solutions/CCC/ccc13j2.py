import sys
input = sys.stdin.readline
s = input().strip('\n')
if s.count('I')+s.count('O')+s.count('S')+s.count('H')+s.count('Z')+s.count('X')+s.count('N')==len(s):
    print('YES')
else:
    print('NO')