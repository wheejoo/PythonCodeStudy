from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b):
    q = deque([[a, b]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                #이동
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

bfs(0,0)
print(graph[n - 1][m - 1]) #문제에서 (1,1), bfs(0,0)설정했기에
