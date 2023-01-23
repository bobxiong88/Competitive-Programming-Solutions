# for each unique number k, find a range where k-nonk is the greatest!
# do this for every k, efficiently
# obs: he will always have at least 2 dollars
# find position of number for each value of k, -1 when not k, this becomes
# the maximum subarray problem!!!->kadane's algorithm
import sys
input = sys.stdin.readline
def maxsub(a,size):
    max_so_far = -float('inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,size):
 
        max_ending_here += a[i][0]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = a[i][1]
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = a[i][1]+1
    return max_so_far,start,end
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    freq = dict()
    for i in range(n):
        if x[i] in freq: freq[x[i]].append(i)
        else: freq[x[i]] = [i]
    s = -float('inf')
    ans = (-float('inf'), 0, 0,0)
    for k in freq.keys():
        curr = freq[k]
        arr = []
        for i in range(len(curr)-1):
            arr.append((1, curr[i]))
            arr.append((-(curr[i+1]-curr[i]-1), 69))
        arr.append((1,curr[-1]))
        s,l,r = maxsub(arr,len(arr))
        ans = max((s,k,l+1,r+1),ans)
    print(*ans[1:])
        
            
