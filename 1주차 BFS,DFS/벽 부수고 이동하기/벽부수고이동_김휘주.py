from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    q = deque()
    q.append((0,0,1))
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        x,y,c = q.popleft() #좌표, 벽 부술 횟수

        if x == n-1 and y == m-1: #끝나는 위치와 같다면
            return visited[x][y][c]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                #벽x 방문한적x
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append((nx, ny, c))
                #벽0 뚫린적x
                elif graph[nx][ny] == 1 and c == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))
    return -1

print(bfs())
