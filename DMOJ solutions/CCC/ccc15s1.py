k = int(input())
a = []
for i in range(k):
    b = int(input())
    if not b: a.pop()
    else: a.append(b)
print(sum(a))