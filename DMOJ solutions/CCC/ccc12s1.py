def f(n):
    ans = 1
    for i in range(1,n+1):
        ans*=i
    return ans
n = int(input())
ans = 0
if n>=4:
    ans = f(n-1)//(f(3)*f(n-4))
print(ans)