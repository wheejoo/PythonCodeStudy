from collections import deque
n,m,k = map(int,input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = []
def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 1
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    cnt += 1
                    q.append((nx,ny))
    result.append(cnt)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i,j)

print(len(result))
result.sort()
for r in result:
    print(r,end = " ")

