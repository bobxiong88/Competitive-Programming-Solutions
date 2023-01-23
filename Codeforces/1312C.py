import sys
input = sys.stdin.readline
def b(n, k):
    if n==0:
        return [0]*100
    digits = []
    while n:
        digits.append(n%k)
        n //= k
    return [0]*(100-len(digits))+digits[::-1]
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    arr = [0 for i in range(101)]
    for v in a:
        curr = b(v, k)
        for i in range(100):
            arr[i] += curr[i]
    ans = 'YES'
    for i in arr:
        if i>1: ans = 'NO'
    print(ans)
