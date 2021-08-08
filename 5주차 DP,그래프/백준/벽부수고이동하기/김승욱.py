# 답지봄
import collections
import sys
input = sys.stdin.readline
dx,dy = [1, -1, 0, 0], [0,0,-1,1]

def bfs():
    queue = collections.deque()
    queue.append((0,0,1))
    visited = [[[0,0] for _ in range(m)] for _ in range(n)] # 
    visited[0][0][1] = 1 # 3중 리스트를 만들어 벽을 부술수 있는지 없는지를 저장한다. 
    # ex) visited[3][5][0]에 들어있는값은 (3,5) 까지 한번 부술수 있는 벽을 부숴 도달한 거리가 들어있다.
    # ex) visited[3][5][1]에 들어있느값은 (3,5) 까지 벽을 부수지 않고 도달한 거리 들어있음 벽 부수기 한번 가능
    while queue:
        x,y,z = queue.popleft()
        if x == n-1 and y == m-1: # 목적지 (x,y) 도착
            print(visited)
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 1: # 벽을 만났고 z == 1 이면 벽을 부술수 있다는 뜻
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx,ny,0))
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0: # 벽이 아니고 visited[nx][ny][z] == 0 은 아직 한번도 안지나간길
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx,ny,z))
    return -1
n, m = map(int,input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs())

# 시간초과
# import collections
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = [list(map(int,input().rstrip())) for _ in range(n)]
# dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
# queue = collections.deque()

# def bfs(x,y):
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         visited[x][y] = True
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<= nx < n and 0<= ny < m:
#                 if graph[nx][ny] == 0 and visited[nx][ny] == False:
#                     visited[nx][ny] = True
#                     distance[nx][ny] = distance[x][y] + 1
#                     queue.append((nx,ny))

# minn = sys.maxsize
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             graph[i][j] = 0
#             visited = [[False]*m for _ in range(n)]
#             distance = [[1] * m for _ in range(n)]
#             bfs(0,0)
#             if distance[n-1][m-1] != 1:
#                 minn = min(minn, distance[n-1][m-1])
#             graph[i][j] = 1

# if minn == sys.maxsize:
#     print(-1)
# else:
#     print(minn)