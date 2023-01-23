import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    k = int(n)
    f = []
    for i in range(2,int(n**0.5)+1):
        cnt = 0
        while n%i == 0:
            cnt += 1
            n//=i
        if cnt:
            f.append([cnt, i])
    if n!=1:
        f.append([1, n])
    f.sort(reverse = True)
    ans = []
    k //= f[0][1]**(f[0][0]-1)
    for i in range(f[0][0]-1):
        ans.append(f[0][1])
    ans.append(k)
    print(len(ans))
    print(*ans)
