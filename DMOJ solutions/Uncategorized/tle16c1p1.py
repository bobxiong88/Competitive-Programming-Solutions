D = int(input())
a = list(map(int,input().split()))
Q = int(input())
b = list(map(int,input().split()))
if 10/max(a) > 25/min(b):
    print("Dimes are better")
elif 25/max(b) > 10/min(a):
    print("Quarters are better")
else:
    print("Neither coin is better")