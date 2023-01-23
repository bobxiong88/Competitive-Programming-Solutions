for _ in range(int(input())):
    y, m, d = map(int,input().split())
    cum = (1989, 2, 27)
    if (y, m, d) <= cum:
        print("Yes")
    else:
        print("No")