import sys
input = sys.stdin.readline
def get(i,j, arr):
    if i == 0:
        return arr[j]
    else:
        return arr[j]-arr[i-1]
s = input().strip('\n')
a = s.count('A')
b = s.count('B')
c = s.count('C')
n = s*2
x = 0
y = 0
z = 0
psA = []
psB = []
psC = []
for i in range(len(n)):
    if n[i] == 'A':
        x += 1
    psA.append(x)
    if n[i] == 'B':
        y += 1
    psB.append(y)
    if n[i] == 'C':
        z += 1
    psC.append(z)
ans = float('inf')
for i in range(len(s)):
    ans = min(ans, a-get(i, i+a-1, psA)+b-get(i+a, i+a+b-1,psB)-min(get(i,i+a-1, psB), get(i+a, i+a+b-1, psA)))
    ans = min(ans, a-get(i, i+a-1, psA)+c-get(i+a, i+a+c-1,psC)-min(get(i,i+a-1, psC), get(i+a, i+a+c-1, psA)))

print(ans)