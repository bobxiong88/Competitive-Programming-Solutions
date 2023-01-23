import sys
input = sys.stdin.readline
l = int(input())
s = int(input())-l
fine = 0
if 1<=s<=20: fine = 100
elif 21<=s<=30: fine = 270
elif 31<=s: fine = 500
if fine: print("You are speeding and your fine is ${f}.".format(f = fine))
else: print("Congratulations, you are within the speed limit!")