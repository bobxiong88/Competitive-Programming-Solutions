import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = [i for i in range(n,0,-1)]
    print(*ans)
        
