N,Q = map(int,input().split())

pile = list(map(int,input().split()))

for i in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        pile[query[1]-1:query[2]] = sorted(pile[query[1]-1:query[2]])
    else:
        pile[query[1]-1:query[2]] = list(reversed(sorted(pile[query[1]-1:query[2]])))
print(" ".join([str(i) for i in pile]))