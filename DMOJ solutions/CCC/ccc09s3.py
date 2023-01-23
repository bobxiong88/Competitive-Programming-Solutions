def friendFriend(visited, graph, node, lisFriend):
  visited.append(node)
  
  queue=[(node,0)]
  
  depth = 0
  
  while queue:
   
    s,d = queue.pop(0)
    
    if d == 2:
        lisFriend.append(0)
    
    try:
        for neighbour in graph[s]:
            
          if neighbour not in visited:
            visited.append(neighbour)
            if d+1>2:
                break
            queue.append((neighbour,d+1))
    except:
        pass

def bfs(visited, graph, node, e):
  visited.append(node)
  
  queue=[(node,0)]

  depth = 0
  
  while queue:
   
    s,d = queue.pop(0)
    
    if d > depth:
        depth+=1
    
    if s == e:
        return depth
        
    
    if s in graph.keys():
        for neighbour in graph[s]:
          if neighbour not in visited:
            visited.append(neighbour)
            queue.append((neighbour,depth+1))
 
    
graph = {1:[6],
         2:[6],
         3:[4,5,6,15],
         4:[3,5,6],
         5:[3,4,6],
         6:[1,2,3,4,5,7],
         7:[6,8],
         8:[7,9],
         9:[8,10,12],
         10:[9,11],
         11:[10,12],
         12:[9,11,13],
         13:[12,14,15],
         14:[13],
         15:[3,13],
         16:[17,18],
         17:[16,18],
         18:[16,17]
         }
while True:
    inp = input()
    if inp == "i":
        f1 = int(input())
        f2 = int(input())
        
        if f1 not in graph.keys():
            graph.update({f1:[f2]})
        else:
            if f2 not in graph[f1]:
                
                graph[f1].append(f2)


        if f2 not in graph.keys():
            graph.update({f2:[f1]})
        else:
            if f1 not in graph[f2]:
                
                graph[f2].append(f1)
            
    if inp == "d":
        f1 = int(input())
        f2 = int(input())

        
        graph[f1].remove(f2)
        graph[f2].remove(f1)

    if inp == "n":
        p = int(input())
        print(len(graph[p]))

    if inp == "f":
        lisFriend = []
        p = int(input())
        friendFriend([], graph, p, lisFriend)
        print(len(lisFriend))
    if inp == "s":
        f1 = int(input())
        f2 = int(input())
        separation = bfs([], graph, f1, f2)
        if separation == None:
            print("Not connected")
        else:
            
            print(separation)

    if inp == "q":
        break