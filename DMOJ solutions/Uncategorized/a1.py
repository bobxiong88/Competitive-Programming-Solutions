for i in range(int(input())):
    p = input()
    k = 0
    a = ''
    while k < len(p) and p[k].isdigit():
        a += p[k]
        k += 1
    a = int(a)
    b = list(p[k+1:])
    del b[a-1]
    print("{} {}".format(i+1,''.join(b)))