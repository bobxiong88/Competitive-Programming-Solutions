N = int(input())
S = input().strip('\n')
freq = [0]*26
for i in S:
    freq[ord(i)-ord('a')]+=1
cnt = 0
for i in freq:
    cnt += i%2
print(max(cnt, 1))