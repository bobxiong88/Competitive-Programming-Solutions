n = int(input())
m = int(input())
a = [input().strip('\n') for i in range(n)]
b = [input().strip('\n') for i in range(m)]
for i in a:
    for j in b:
        print(i, 'as', j)