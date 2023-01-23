for i in range(int(input())):
    s = 0
    for j in range(int(input())):
        s += int(input())
    if s == 0:
        print('Weekend')
    else:
        print('Day {}: {}'.format(i+1,s))