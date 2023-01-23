import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    cnt = dict()
    for i in range(n):
        s = input().strip('\n')
        for j in s:
            try: cnt[j]+=1
            except: cnt[j] = 1
    ans = True
    for i in cnt:
        if cnt[i]%n:
            ans = False
    if ans:
        print("YES")
    else:
        print("NO")
    
