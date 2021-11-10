def BFS(maze, start, end):
    route = []
    frontier = [start]
    visited = [start]
    bfsPath = {}
    travel_path = []
    while len(frontier) > 0:
        curPos = frontier.pop(0)
        travel_path.append(curPos)
        if curPos == end:
            break
        directions = [(curPos[0]-1,curPos[1]),(curPos[0]+1,curPos[1]),(curPos[0],curPos[1]-1),(curPos[0],curPos[1]+1)]
        for nextPos in directions:
            if nextPos not in visited:
                if maze[nextPos[0]][nextPos[1]] == ' ':
                    frontier.append(nextPos)
                    visited.append(nextPos)
                    bfsPath[nextPos] = curPos
            else:
                continue
    
    cur_point = end
    route.append(end)
    while cur_point != start:
        route.append(bfsPath[cur_point])
        cur_point = bfsPath[cur_point]
    route.reverse()
    return route, visited
