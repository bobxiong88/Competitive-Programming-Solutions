import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())
    y = 0
    for i in range(32):
        if (x>>i)&1:
            y |= 1<<i
            break
    if bin(x).count("1") == 1:
        for i in range(32):
            if not (x>>i)&1:
                y|=1<<i
                break
    print(y)
        
