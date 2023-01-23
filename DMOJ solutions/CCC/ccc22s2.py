import sys
input = sys.stdin.readline
X = int(input())
same = set()
for i in range(X):
    a, b = input().split()
    if a > b : a, b = b, a
    same.add((a,b))
Y = int(input())
diff = set()
for i in range(Y):
    a, b = input().split()
    if a > b: a, b = b, a
    diff.add((a,b))
G = int(input())
groups = set()
c = 0
for x in range(G):
    names = sorted(list(input().split()))
    for i in range(2):
        for j in range(i+1, 3):
            groups.add((names[i],names[j]))
            if (names[i],names[j]) in diff:
                c += 1
for x in same:
    if x not in groups:
        c += 1
print(c)