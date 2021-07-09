import collections
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]

queue = collections.deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and distance[nx][ny] == 0:
                    graph[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            queue.append((x,y))

bfs()
checker = True
for i in graph:
    if 0 in i:
        print(-1)
        checker = False
        break

curMax = 0
for i in distance:
    curMax = max(curMax, max(i))

if checker:
    print(curMax)