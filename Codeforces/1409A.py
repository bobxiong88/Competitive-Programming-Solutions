import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = map(int,input().split())
    diff = abs(b-a)
    ans = diff//10
    if diff%10: ans+=1
    print(ans)
