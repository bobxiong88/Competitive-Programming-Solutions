import sys
input = sys.stdin.readline
s = input().strip('\n')
letters = set()
for i in s:
    letters.add(i)
if len(letters)&1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")