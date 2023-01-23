numBoards = int(input())

boards = list(map(int,input().split()))

cnt = [0]*2001
for i in boards:cnt[i]+=1

heights= [0 for i in range(4001)]

for i in range (2001):
    for j in range(i,2001):
        if cnt[i] and cnt[j]:
            if i==j:
                heights[i+j] += (cnt[i]//2)
            else:
                heights[i+j] += min(cnt[i], cnt[j])

print(str(int(max(heights)))+" "+str(heights.count(max(heights))))