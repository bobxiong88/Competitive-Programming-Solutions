t1 = int(input())
t2 = int(input())
t3 = 0
l = 0

while t1 >= t2:
    t3 = t1 - t2
    t1 = t2
    t2 = t3
    l = l + 1

print(l+2)