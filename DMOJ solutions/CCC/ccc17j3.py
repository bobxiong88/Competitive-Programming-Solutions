a,b = map(int,input().split())
c,d = map(int,input().split())
n = int(input())
s = abs(c-a)+abs(d-b)
ans = 'Y'
if s%2!=n%2 or n<s: ans = 'N'
print(ans)