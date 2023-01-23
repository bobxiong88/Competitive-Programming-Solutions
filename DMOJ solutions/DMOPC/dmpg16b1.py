a = [5, 10, 25, 100, 200]
b = list(map(int,input().split()))
print(sum([a[i]*b[i] for i in range(5)]))