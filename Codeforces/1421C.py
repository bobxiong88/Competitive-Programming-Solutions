import sys
input = sys.stdin.readline
def R(a):
    return 'R {}'.format(a)
def L(a):
    return 'L {}'.format(a)
s = input().strip('\n')
n = len(s)
cmd = []
cmd.append(R(2))
cmd.append(L(n))
cmd.append(L(n-1))
print(3)
print('\n'.join(cmd))
