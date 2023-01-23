h = int(input())
M = int(input())

t = 1
A = 1000000
s = "The balloon first touches ground at hour:"

while t < M and A > 0:
    A = -6*t**4 + h*t**3 + 2*t**2 + t
    t = t + 1

if A > 0:
    print("The balloon does not touch ground in the given time.")
else:
    print(s)
    print(t-1)