a = float(input())
b = float(input())
ans = 0
if not a and not b:
    ans = 'indeterminate'
elif not a:
    ans = 'undefined'
else:
    ans = '{:.2f}'.format(round(-b/a,2))
print(ans)