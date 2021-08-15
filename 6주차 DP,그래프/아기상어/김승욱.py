# 모르겠다, 다시풀어보기

import collections

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = collections.deque()
count = 0
def bfs(a,b):
    baby = 2
    baby_cnt = 0
    global count
    queue.append((a,b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0 and graph[nx][ny] < baby and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    count += 1
                    baby_cnt += 1
                    if baby_cnt == baby:
                        baby += 1
                        baby_cnt = 0
                    queue.append((nx,ny))
                elif (graph[nx][ny] == 0 or graph[nx][ny] == baby) and visited[nx][ny] == False:
                    count += 1
                    queue.append((nx,ny))

for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            bfs(x,y)
maxx = 0
for i in distance:
    maxx = max(maxx,max(i))
print(count)