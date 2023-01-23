import sys
input = sys.stdin.readline
def base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
for _ in range(int(input())):
    n = int(input())
    curr = "11"
    for i in range(33):
        a = int(curr, 2)
        if n%a==0:
            print(n//a)
            break
        curr = curr + "1"
