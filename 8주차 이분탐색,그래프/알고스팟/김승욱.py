# appendleft 생각못했다..

import collections
m,n = map(int, input().split())

graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
distance = [[0]*m for _ in range(n)]
dx,dy = [-1,1,0,0], [0, 0, -1, 1]
queue = collections.deque()

def bfs():
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        if x == n-1 and y == m-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y]
                    queue.appendleft((nx,ny)) # 0 인 곳을 먼저 탐색하기위해서 appendleft
                elif graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))

bfs()
print(distance[n-1][m-1])