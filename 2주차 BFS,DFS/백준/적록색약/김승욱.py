import collections

n = int(input())

graph = [list(input()) for _ in range(n)]
check = [[False]*n for _ in range(n)]
queue = collections.deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x,y):
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and check[nx][ny] == False:
                    check[nx][ny] = True
                    queue.append((nx,ny))

count1=0
count2=0
for x in range(n):
    for y in range(n):
        if check[x][y] == False:
            count1 += 1
            bfs(x,y)
            
for x in range(n):
    for y in range(n):
        if graph[x][y] == 'G':
            graph[x][y] = 'R'

check = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if check[x][y] == False:
            count2 += 1
            bfs(x,y)
            
print(count1, count2)

