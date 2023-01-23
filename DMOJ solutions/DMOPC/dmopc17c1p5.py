import sys
input = sys.stdin.readline
def find(v):
    left, right = 0, len(stack)-1
    if stack[-1][1]>=v: return 1
    if stack[0][1]<=v: return len(stack)
    if right==0: return 1
    while 1:
        middle = (left+right)//2
        if stack[middle][1] == v: return len(stack)-middle
        if middle+1<=len(stack)-1:
            if stack[middle][1] > v and stack[middle+1][1] < v: return len(stack)-(middle+1)
        if middle-1>=0:
            if stack[middle][1] < v and stack[middle-1][1] > v: return len(stack)-middle
        if stack[middle][1] > v: left = middle + 1
        elif stack[middle][1] < v: right = middle - 1
N, Q = map(int,input().split())
a, q = [int(i) for i in input().split()], [[] for i in range(N)]
for i in range(Q):
    l,r = [int(i)-1 for i in input().split()]
    q[l].append((r,i))
ans, stack = [0 for i in range(Q)], []
for i in range(-1,-N-1, -1):
    i+=N
    while stack and stack[-1][0]<a[i]:
        stack.pop()
    stack.append((a[i],i))
    for r, x in q[i]: ans[x] = str(find(r))
print("\n".join(ans))