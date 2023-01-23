import sys
input = sys.stdin.readline
def solution(n):
    n = int(n)
    step = 0
    while n!=0:
        if n%2==0:
            n/=2
        else:
            if n==3 or n%4==1:
                n-=1
            else:
                n+=1
        step+=1
    return step
T = int(input())
for _ in range(T):
    print(solution(int(input())))