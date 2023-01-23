import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    n = len(s)
    R, P, S = s.count('R'), s.count('P'), s.count('S')
    if max(R,P,S) == R: print('P'*n)
    elif max(R, P, S) == P: print('S'*n)
    else: print('R'*n)
