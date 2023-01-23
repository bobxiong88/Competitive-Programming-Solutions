import sys
input = sys.stdin.readline
def query(a,b):
    print("? {} {}".format(a, b))
    sys.stdout.flush()
    return int(input())
def ans(x):
    print("! {}".format(x))
    sys.stdout.flush()
    sys.exit(0)
for i in range(25):
    a = query(i+1,i+2)
    b = query(i+2,i+1)
    if a == -1 or b == -1:
        ans(i+1)
    if a != b:
        ans(a+b)
