# bfs 구현문제
# 이런문제도 점점 익숙해지는것 같다..

import collections

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
queue = collections.deque()

def bfs(Dx,Dy):
    while queue:
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[x][y] == 'S' and (graph[nx][ny] =='.' or graph[nx][ny] == 'D'):
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                elif graph[x][y] == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'S'):
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            queue.append((i,j))
        if graph[i][j] == 'D':
            Dx, Dy = i,j

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            queue.append((i,j))

print(bfs(Dx,Dy))