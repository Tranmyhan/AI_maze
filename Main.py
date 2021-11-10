
import Map_Visualize as mv
import DFS as dfs
import BFS as bfs
from queue import PriorityQueue

diem, maze = mv.read_file('maze.txt')
#bonus_points, matrix = mv.read_file('maze_map.txt')



def start_end_point(matrix):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i,j)
            elif i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1:
                if maze[i][j]==' ':
                    end = (i,j)
    return start, end

starts, ends = start_end_point(maze)


print(f'the height of the matrix: {len(maze)}')
print(f'the width of the matrix: {len(maze[0])}')


#route1, path1 = dfs.DFS(maze, starts, ends)
#print(route1)
#print(path1)

#print('nowwwwwww BFSSSSSSS')

#route, path = bfs.BFS(maze, starts, ends)
#print(route)
#print(path)

#print(len(path1))
#print(len(path))


def heu_cost(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return abs(x1-x2) + abs(y1-y2)

def AStar(maze, start, end):
    route = []
    path = []
    aPath = {}

    ways = [(i,j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j]== ' ']
    g_score = {pos:float('inf') for pos in ways}
    g_score[start] = 0
    f_score = {pos:float('inf') for pos in ways}
    f_score[start] = heu_cost(start,end)
    
    frontier = PriorityQueue()
    frontier.put((heu_cost(start,end), heu_cost(start,end),start))

    while not frontier.empty():
        curPos = frontier.get()[2]
        path.append(curPos)
        if curPos == end:
            break
        directions = [(curPos[0]-1,curPos[1]),(curPos[0]+1,curPos[1]),(curPos[0],curPos[1]-1),(curPos[0],curPos[1]+1)]
        for nextPos in directions:
            if maze[nextPos[0]][nextPos[1]] == ' ':
                tmp_g_score = g_score[curPos] + 1
                tmp_f_score = tmp_g_score + heu_cost(nextPos,end)
                if tmp_f_score < f_score[nextPos]:
                    g_score[nextPos] = tmp_g_score
                    f_score[nextPos] = tmp_f_score
                    frontier.put((tmp_f_score,heu_cost(nextPos,end),nextPos))
                    aPath[nextPos] = curPos
    cur_point = end
    route.append(end)
    while cur_point != start:
        route.append(aPath[cur_point])
        cur_point = aPath[cur_point]
    route.reverse()
    return route, path


route, path = AStar(maze, starts, ends)
print(route)
print(path)

mv.visualize_maze(maze,diem,starts,ends, route, path)