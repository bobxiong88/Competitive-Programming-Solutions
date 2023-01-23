n = int(input())
a = input().strip('\n')
b = input().strip('\n')
c = 0
for i in range(n):
    if a[i] == b[i] == 'C': c+=1
print(c)