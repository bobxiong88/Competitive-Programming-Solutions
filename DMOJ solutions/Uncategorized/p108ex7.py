from math import ceil
for _ in range(int(input())):
    n = int(input())
    if n in range(0,31): n = 38
    elif n in range(31,51): n = 55
    elif n in range(51,101): n = 73
    else: n = 73+24*ceil((n-100)/50)
    print(n)