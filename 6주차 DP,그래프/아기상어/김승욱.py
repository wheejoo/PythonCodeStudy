# 구현이 어려웠던 문제..

import collections

n = int(input())
answer = 0
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]

size = 2
exp = 0

def bfs(a,b,size):
    queue = collections.deque()
    queue.append((a,b))
    visited[a][b] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (graph[nx][ny] == size or graph[nx][ny] == 0) and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                elif graph[nx][ny] < size and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                    result.append([distance[nx][ny], nx, ny])
while True:
    result = []
    visited = [[False]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 9:
                bfs(x,y,size)
                graph[x][y] = 0
    if result:
        result.sort()
        dis,r_x,r_y = result.pop(0)
        exp += 1
        answer += dis
        graph[r_x][r_y] = 9
    else:
        break
    if exp == size:
        size += 1
        exp = 0
print(answer)