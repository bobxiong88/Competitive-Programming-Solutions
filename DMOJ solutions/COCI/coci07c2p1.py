a = list(map(int,input().split()))
b = [1, 1, 2, 2, 2, 8]
print(*[b[i]-a[i] for i in range(6)])