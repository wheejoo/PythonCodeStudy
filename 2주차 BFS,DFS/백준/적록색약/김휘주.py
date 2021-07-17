from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
graph_rg = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(a,b,arr,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == arr:
                    visited[nx][ny] = 0
                    q.append((nx,ny))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            graph_rg[i][j] = 'R'
        else:
            graph_rg[i][j] = 'B'

cnt = 0
cnt_rg = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            cnt += 1
            bfs(i,j,graph[i][j],graph)
        if graph_rg[i][j] != 0:
            cnt_rg += 1
            bfs(i,j,graph_rg[i][j],graph_rg)
print(cnt, cnt_rg)

