for _ in range(int(input())):
    x = int(input())
    if x in range(80,101):
        ans = 'A'
    elif x in range(70,80):
        ans = 'B'
    elif x in range(60,70):
        ans = 'C'
    elif x in range(50,60):
        ans = 'D'
    elif x in range(0,50):
        ans = 'F'
    else:
        ans = 'X'
    print(ans)