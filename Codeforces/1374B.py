import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    two = 0
    while n%2==0:
        n/=2
        two+=1
    three = 0
    while n%3==0:
        n/=3
        three+=1
    if n!=1 or two>three:
        print(-1)
        continue
    print(three-two+three)
