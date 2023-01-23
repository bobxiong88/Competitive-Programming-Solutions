n = int(input())


for _ in range(n):
    graph = {}
    
    r = int(input())
    c = int(input())

    pr = r-int(input())
    pc = int(input())-1

    kr = r-int(input())
    kc = int(input())-1

    board = [[100 for x in range(c)] for y in range(r)]

    board[kr][kc] = 0
    queue = [[kr,kc]]
    stale = -1
    win = False
    while queue:
        y,x = queue.pop(0)

        possible = []
        possible.append([y+2,x+1])
        possible.append([y+1,x+2])
        possible.append([y-1,x+2])
        possible.append([y-2,x+1])
        possible.append([y-2,x-1])
        possible.append([y-1,x-2])
        possible.append([y+1,x-2])
        possible.append([y+2,x-1])

        for p in possible:
            if p[0]>=0 and p[0]<=r-1 and p[1]>=0 and p[1]<=c-1:
                if board[p[0]][p[1]]>board[y][x]+1:
                    board[p[0]][p[1]] = board[y][x]+1
                    queue.append(p)
                
    
    for y in range(pr):
        if board[pr-y][pc] == y or (y-board[pr-y][pc])%2 ==0 and board[pr-y][pc]<y:
            win = y
            break
        elif board[pr-y-1][pc] == y and stale == -1:
            stale = y
    if win:
        print("Win in",win,"knight move(s).")
    elif stale != -1:
        print("Stalemate in",stale,"knight move(s).")
    else:
        print("Loss in",y,"knight move(s).")