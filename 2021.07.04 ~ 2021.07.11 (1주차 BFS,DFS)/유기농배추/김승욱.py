import collections

t = int(input())


def bfs(x,y):
    queue = collections.deque()
    queue.append((x,y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and check[nx][ny] == -1:
                    check[nx][ny] = 1
                    queue.append((nx,ny))
    
for i in range(t):
    n, m, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    check = [[-1]*m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    count = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1 and check[x][y] == -1:
                bfs(x,y)
                count += 1
    print(count)

