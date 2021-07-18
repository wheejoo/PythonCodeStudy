import collections

m, n, k = map(int, input().split()) # m 세로, n 가로

graph = [[0]*n for _ in range(m)]
check = [[False]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            graph[x][y] = 1


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x,y):
    total = 0
    
    queue = collections.deque()
    queue.append((x,y))
    while queue:
        total += 1
        check[x][y] = True
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0 and check[nx][ny] == False:
                    check[nx][ny] = True
                    queue.append((nx,ny))
    return total

count = 0
result = []
for x in range(m):
    for y in range(n):
        if graph[x][y] == 0 and check[x][y] == False:
            result.append(bfs(x,y))
            count+=1
result.sort()
print(count)
for i in result:
    print(i, end=' ')