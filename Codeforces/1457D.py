import sys
input = sys.stdin.readline
from math import log
from math import floor
def b(x): return bin(x)[2:]
n = int(input())
if n>=64:
    print(1)
    sys.exit(0)
a = list(map(int,input().split()))
ans = float('inf')
for i in range(n-1):
    left = []
    right = []
    curr = 0
    for j in range(i,-1,-1):
        curr ^= a[j]
        left.append((curr, i-j))
    curr = 0
    for j in range(i+1,n):
        curr ^= a[j]
        right.append((curr, j-i-1))
    #print(left)
    #print(right)
    for aa,x in left:
        for bb,y in right:
            if aa > bb:
                ans = min(ans, x+y)
if ans == float('inf'): ans = -1
print(ans)
'''
- a number can only be greater than another through xoring iff
it has equal number of bits

- two numbers with equal number of bits xor to smaller number
- xor is communative and associative
- 3 consecutive numbers with same number of bits, the answer is at most 1
- no consecutive is impossilbe
- for N>64, the answer MUST be 1

'''
