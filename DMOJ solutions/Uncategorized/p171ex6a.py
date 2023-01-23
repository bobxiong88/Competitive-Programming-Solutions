ans = -float('inf')
for i in range(int(input())):
    ans = max(ans,float(input()))
print('{:.4f}'.format(ans))