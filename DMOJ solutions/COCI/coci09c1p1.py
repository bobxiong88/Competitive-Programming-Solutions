a = list(map(int,input().split()))
b = sorted(a)
ans = 'mixed'
if a == b:
    ans = 'ascending'
elif a == b[::-1]:
    ans = 'descending'
print(ans)