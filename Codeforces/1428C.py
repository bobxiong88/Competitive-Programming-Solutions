import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip('\n')
    ans = 0
    for i in s:
        if i == 'B' and ans!=0:
            ans -= 1
        else:
            ans+=1
    print(ans)
