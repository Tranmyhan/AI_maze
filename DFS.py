def DFS(matrix, start, end):
    route = []
    travel_path = []
    if start == end:
        route.append(start)
        return route
    
    stack_frontier = []
    list_explore = []
    dfspath = {}
    stack_frontier.append(start)
    while len(stack_frontier) != 0:
        cur_point = stack_frontier.pop()
        travel_path.append(cur_point)
        if cur_point == end:
            break        
        neighbour = [(cur_point[0]-1,cur_point[1]),(cur_point[0]+1,cur_point[1]),(cur_point[0],cur_point[1]-1),(cur_point[0],cur_point[1]+1)]
        for point_next in neighbour:
            if point_next not in list_explore:
                if matrix[point_next[0]][point_next[1]] == ' ':
                    stack_frontier.append(point_next)
                    list_explore.append(point_next)
                    dfspath[point_next] = cur_point
    cur_point = end
    route.append(end)
    while cur_point != start:
        route.append(dfspath[cur_point])
        cur_point = dfspath[cur_point]
    route.reverse()
    return route, travel_path