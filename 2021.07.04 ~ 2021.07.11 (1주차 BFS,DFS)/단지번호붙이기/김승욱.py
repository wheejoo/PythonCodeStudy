import collections

n = int(input())

graph = [list(map(int,input().strip())) for _ in range(n)]

check = [[False]*n for _ in range(n)]

def bfs(x,y):
    count = 1
    check[x][y] = True
    queue = collections.deque()
    queue.append((x,y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and check[nx][ny] == False:
                    count += 1
                    check[nx][ny] = True
                    queue.append((nx,ny))
    return count


result = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and check[x][y] == False:
            result.append(bfs(x,y))
            
print(len(result))
result.sort()
for i in result:
    print(i)
