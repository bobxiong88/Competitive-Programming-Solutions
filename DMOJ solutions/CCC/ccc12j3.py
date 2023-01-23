grid = [list('*x*'), list(' xx'), list('* *')]
k = int(input())
for i in range(3):
    for j in range(3):
        grid[i][j] = k*grid[i][j]
for i in range(3):
    for j in range(k):
        print(''.join(grid[i]))