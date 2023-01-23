curr = 1
m = [i for i in range(101)]
m[54], m[90], m[99] = 19, 48, 77
m[9], m[40], m[67] = 34, 64, 86
while True:
    a = int(input())
    if not a:
        print("You Quit!")
        break
    if curr+a<=100: curr += a
    curr = m[curr]
    print("You are now on square {}".format(curr))
    if curr == 100:
        print("You Win!")
        break