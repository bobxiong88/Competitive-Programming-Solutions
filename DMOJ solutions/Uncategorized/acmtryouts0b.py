t = int(input())


for i in range(t):
    n = int(input())
    f1 = list(input())
    f2 = list(input())
    f3 = []
    while len(f1) > 0:
        a = f1[-1]
        b = f2[-1]
        f3.append(b)
        f3.append(a)
        f1.pop(-1)
        f2.pop(-1)
    print(''.join(f3))