for i in range(int(input())):
    n = int(input())
    while n>=10:
        n = sum(list(map(int,list(str(n)))))
    print(n)