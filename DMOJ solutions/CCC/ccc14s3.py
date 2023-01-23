import sys
for _ in range(int(input())):
    n = int(input())
    a = [int(input()) for i in range(n)][::-1]
    curr = 0
    stack = []
    for i in a:
        stack.append(i)
        if i == curr+1:
            while stack and stack[-1] == curr+1:
                stack.pop()
                curr+=1
    print('Y' if not stack else 'N')